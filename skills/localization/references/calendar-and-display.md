# 预约时间与完整消息

## 教学场景

一个预约产品面向不同语言和时区的用户。旧实现保存“10/11 9:00”这样的显示字符串，后端重新解析，浏览器再根据本机时区修改。通知和页面各自拼接“已预约”加数量，语言切换后出现混合文本。

先确定时间的业务含义。一次发生的预约保存明确的时间点与所需时区信息；每周当地九点的循环规则保存当地时间、时区和重复规则。全天日期直接使用日期语义。把三类对象统一转成一个随意解析的字符串，会丢失决定性信息。

## 显示使用语言与时区

用户语言和展示时区可以独立选择。下面把一个确定时间点按指定语言和时区显示，交给标准 Intl 格式化：

```javascript
function appointmentLabel(instantIso, locale, timeZone) {
  const instant = new Date(instantIso);
  if (Number.isNaN(instant.getTime())) {
    throw new RangeError("Invalid appointment instant");
  }
  return new Intl.DateTimeFormat(locale, {
    timeZone,
    dateStyle: "medium",
    timeStyle: "short",
  }).format(instant);
}
```

输入契约要求带明确偏移量或 `Z` 的时间点。不要把缺少时区的本地字符串交给不同机器猜测。Intl 行为见 [ECMA-402](https://tc39.es/ecma402/#datetimeformat-objects)。

循环预约遇到夏令时缺失或重复时刻时，需要产品确定跳过、顺延或选择某个偏移的规则，再由成熟时间库执行。页面把用户选择传给业务所有者，禁止每个入口独立修补一小时。

## 翻译整条消息

将“成功处理几个文件、失败几个、怎样恢复”写成完整资源消息。数量、对象和链接作为参数，复用项目现有消息格式化器及复数规则。参考 [ICU MessageFormat](https://unicode-org.github.io/icu/userguide/format_parse/messages/)。

```text
itemsSelected:
  zh-CN: 已选择 {count} 项
  en: {count, plural, one {# item selected} other {# items selected}}
```

这段是资源内容示意，按已采用库的语法接入。语言切换更新所有用户可见状态，包括失败、空状态、按钮和辅助技术标签。领域错误码保持稳定，展示边界决定译文；日志和用户文案分开维护。

## 实际界面需要承受翻译变化

文本变长时让按钮和布局适应内容；数字、货币和日期使用格式化器。支持右至左语言时，检查文本方向和交互方向，使用已有组件能力。用户内容保持其原始语言，禁止把不可翻译文本塞入拼接资源。

检查一次创建、查看、取消路径在目标语言及时区中的一致性。保留真实有意义的日期边界案例，删除各组件独立日期解析器、硬编码译文和重复数字格式化函数。完成当前支持语言后结束，避免制造没有需求的语言管理后台。
