from lxml import etree

html = """
<html>
 <body>
  <div class="job">
   <h2>Python工程师</h2>
   <p class="salary">20-30K</p>
   <p class="city">北京</p>
  </div>
  <div class="job">
   <h2>Java开发</h2>
   <p class="salary">15-25K</p>
   <p class="city">上海</p>
  </div>
 </body>
</html>
"""


#解析HTML
tree = etree.HTML(html)

#提取所有职位
jobs = tree.xpath("//div[@class='job']")
for job in jobs:
    print("========", job.xpath(".//h2/text()"))
    title = job.xpath(".//h2/text()")[0]
    salary = job.xpath(".//p[@class='salary']/text()")[0]
    city = job.xpath(".//p[@class='city']/text()")[0]
    print(f"标题: {title}, 薪资: {salary}, 城市: {city}")