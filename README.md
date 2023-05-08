# hacker-deadlines

帮助安全研究人员追踪黑客会议的截稿日期。

[点击查看详情](./ddl.md)

## 增加/更新 会议

欢迎一起帮忙维护会议的相关信息！

增加或删除会议信息：
- Fork 这个仓库
- 增加/更新 yml 文件 conference/conf_name.yml
- 提交 pull request

## 会议录入文件

示例文件: conference/blackhat-usa.yml

```
- title: Black Hat USA
  description: Black Hat USA
  confs:
    - year: 2023
      id: us-23
      link: https://www.blackhat.com/us-23/
      timeline:
        - deadline: '2023-04-12 23:59:59'
          comment: 'first round'
      timezone: UTC-8
      date: August 9 - August 10, 2023
      place: Mandalay Bay Convention Center, Las Vegas, NV
```

字段描述：

<table>
   <tr>
      <th colspan="3">字段名</th>
      <th>描述</th>
   </tr>
   <tr>
      <td colspan="3"><code>title</code>*</td>
      <td>缩写的会议名称, 不需要年份, 大写</td>
   </tr>
   <tr>
      <td colspan="3"><code>description</code>*</td>
      <td>介绍, 或全称, 无需第几届</td>
   </tr>
   <tr>
      <td rowspan="9"><code>confs</code></td>
      <td colspan="2"><code>year</code>*</td>
      <td>会议的年份</td>
   </tr>
   <tr>
      <td colspan="2"><code>id</code>*</td>
      <td>会议名字和年份, 小写</td>
   </tr>
   <tr>
      <td colspan="2"><code>link</code>*</td>
      <td>会议首页的URL</td>
   </tr>
   <tr>
      <td rowspan="2"><code>timeline</code>*</td>
      <td><code>deadline</code>*</td>
      <td>截稿日期, 格式为 <code>yyyy-mm-dd hh:mm:ss</code> or <code>TBD</code></td>
   </tr>
   <tr>
      <td><code>comment</code></td>
      <td>额外的一些辅助信息, 可选填</td>
   </tr>
   <tr>
      <td colspan="2"><code>timezone</code>*</td>
      <td>截稿日期的时区, 目前支持 <code>UTC-12</code> ~ <code>UTC+12</code> & <code>AoE</code></td>
   </tr>
   <tr>
      <td colspan="2"><code>date</code>*</td>
      <td>会议举办的日期, 示例, Mar 12-16, 2021</td>
   </tr>
   <tr>
      <td colspan="2"><code>place</code>*</td>
      <td>会议举办的地点, 示例, <code>city, country</code></td>
   </tr>
</table>

## 会议清单

- [Black Hat USA](https://www.blackhat.com/us-23/)
- [Black Hat Asia](https://www.blackhat.com/asia-23/)
- [Black Hat Europe](https://www.blackhat.com/eu-22/)

## 关注我们

[VulnTotal安全](https://github.com/VulnTotal-Team)致力于分享高质量原创文章和开源工具，包括物联网/汽车安全、移动安全、网络攻防等。

MIT License

[![Stargazers over time](https://starchart.cc/VulnTotal-Team/hacker-deadlines.svg)](https://starchart.cc/VulnTotal-Team/hacker-deadlines)
