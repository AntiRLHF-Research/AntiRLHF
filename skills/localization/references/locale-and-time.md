# 地区格式、时区和真实含义

## 保持数据本身清楚

时间点、日历日期和持续时长使用相应类型。用户选择的“今天”依其实际时区解释，持久化语义由领域要求决定。展示时使用用户地区与时区，禁止把时间戳简单截字符串当作通用日期。

金额保存数值与币种，计量保存数值与单位。不要将本地化字符串写回业务计算，避免逗号、小数点或符号导致错误解析。

## 使用运行时格式器

```javascript
const formatDate = new Intl.DateTimeFormat(locale, {
  dateStyle: 'medium',
  timeStyle: 'short',
  timeZone,
});
const label = formatDate.format(instant);
```

由当前用户偏好提供 `locale` 与 `timeZone`，由领域提供有效时间点。具体 UI 只显示对使用者有用的信息，禁止把所有格式配置解释成一段操作旁注。

## 切换与回退

资源缺失按项目约定回退到可用语言，关键操作应有完整文案。语言切换更新所有实际呈现者，避免页面和通知各有一份不同偏好。服务端生成内容时明确采用哪一位使用者的地区设置。

## 观察实际结果

检查产品需要的语言和布局：较长文本是否可读、数字与单位是否正确、日期是否按所选时区、错误是否仍然可处理。成熟库已经提供的地区规则直接复用，测试只保护自己的参数和界面接线。

技术参考：[JavaScript Intl](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)。
