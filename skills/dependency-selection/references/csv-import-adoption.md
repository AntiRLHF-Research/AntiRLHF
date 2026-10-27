# 采用成熟解析器：CSV 导入的完整接入

## 教学场景

采购导入器用 `line.split(",")` 读取 CSV。引用字段、字段内换行和引号逐渐导致故障，项目已经出现多个预处理函数和兼容分支。目标是可靠导入商品编码与数量；代码语言为 Python。

先检查现有依赖和标准库。采用 `csv` 处理记录边界、引用与转义，项目继续拥有表头、商品标识和数量规则。不要再写一个 CSV 状态机，也无需为这一项需求新增数据分析框架。

## 完整接入示例

下面是可独立使用的领域解析函数。文件编码由导入入口确定；这里使用 UTF-8 并接受常见 BOM。导入操作可以在外层事务中消费迭代器，出现任意错误时回滚本次写入。

```python
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

@dataclass(frozen=True)
class ImportItem:
    sku: str
    quantity: int

class ImportFormatError(ValueError):
    pass

def read_items(path: Path) -> Iterator[ImportItem]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = csv.reader(stream, strict=True)
        try:
            header = next(rows, None)
            if header != ["sku", "quantity"]:
                raise ImportFormatError("表头应为 sku,quantity")
            for fields in rows:
                end_line = rows.line_num
                if len(fields) != 2:
                    raise ImportFormatError(f"截至第 {end_line} 行的记录应有两列")
                sku, raw_quantity = (value.strip() for value in fields)
                if not sku:
                    raise ImportFormatError(f"截至第 {end_line} 行的商品编码为空")
                try:
                    quantity = int(raw_quantity)
                except ValueError as exc:
                    raise ImportFormatError(
                        f"截至第 {end_line} 行的数量应为整数"
                    ) from exc
                if quantity <= 0:
                    raise ImportFormatError(f"截至第 {end_line} 行的数量应大于零")
                yield ImportItem(sku=sku, quantity=quantity)
        except csv.Error as exc:
            raise ImportFormatError(
                f"CSV 记录格式错误，结束位置约在第 {rows.line_num} 行"
            ) from exc
```

调用方会提前停止读取时，用 `contextlib.closing(read_items(path))` 管理迭代器，及时释放文件；正常导入在事务内消费完整结果。文件访问或解码错误由导入入口映射为具体用户错误，不伪装成空导入成功。字段内换行会使一条记录跨越多个物理行，因此示例使用记录结束行。商品是否存在、重复商品如何合并由导入业务服务处理，不能塞进通用 CSV 规则。

`csv.reader` 的引用、换行和输入约定见 [Python csv 官方文档](https://docs.python.org/3.13/library/csv.html)。项目测试覆盖自己的表头契约、数量规则、错误映射和事务接入；依赖内部的引用算法交给上游。

## 替换到实际入口

让 Web 上传和 CLI 文件导入使用同一解析及业务操作。删除旧 `split` 实现、引号修补、行拼接和只服务这些函数的测试。用户仍在使用另一种文件格式时，在输入边界单独选用对应解析器，内部统一使用 `ImportItem`。

真实导入路径还包括权限、上传大小和写入策略。产品规定全文件原子导入时，迭代读取期间也必须处于对应事务；大型导入若需要分块提交，要明确部分成功的产品语义。不要因为使用生成器就隐式改变提交保证。

## 用实际收益结束选择

完成后导入器只维护业务规则，格式解析由成熟实现承担，两个入口得到相同结果。恢复此前出错的真实文件，观察记录进入业务系统；无需重复证明标准库的每条引用规则，也无需保留第二套解析器供长期对照。
