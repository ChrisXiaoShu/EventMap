# Taiwan Government Event Map
## Why
There is plenty useful activity information in every county and city website. Some of the activities are season traveling info, some are competition event, other mybe exhibition informatioin. However each county or city government has there own website, they only publish the info in their platform. For those people who want to know all the evnet, they have to go through the different wesite. It is not convenient. Therefor, this project ( EventMap ) is trying to solve this problem. The idea is to collect all the infomation from every county and city government website by web crawl, and publish the data in one organize website by using map like format. 
[Web Demo](https://chrisxiaoshu.github.io/EventMap/)  \

## How
### Front-end
- programming language
  javascript、html、css
- envirunment 
  using github.io estabish static web site. The back-end application will run the crawler and push the newest infomation in github to update the map.
- [reference](https://github.com/kiang/bribes_map)
- [detail](https://github.com/ChrisXiaoShu/EventMap/wiki)
### back-end
- using python to develop web cralwer script
- running script on GCP server
- running and monitor cralwer script by MQ server structure 
- using google map API
- store data by sqlite database
- [detail](https://github.com/ChrisXiaoShu/EventMap/wiki)
### crawler target
- [X] [Taipei Travel](https://www.travel.taipei/zh-tw/event-calendar/2020)
- [ ] [Taipei Gov Activity](https://www.gov.taipei/ActivityTheme3.aspx?n=B1167F83E1FE0CD9&sms=9D72E82EC16F3E64)
- [ ] [New Taipei Gov travel information](https://www.ntpc.gov.tw/ch/home.jsp)


