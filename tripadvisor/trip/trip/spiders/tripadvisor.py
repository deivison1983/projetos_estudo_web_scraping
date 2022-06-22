import scrapy
from ..items import TripItem

class TripadvisorSpider(scrapy.Spider):
    name = 'tripadvisor'
    allowed_domains = ['tripadvisor.com.br']
    start_urls = ['https://www.tripadvisor.com.br/Attraction_Review-g303441-d553398-Reviews-Parque_Barigui-Curitiba_State_of_Parana.html']

    def parse(self, response):
    	item = TripItem()
    	quadro_comentarios = response.xpath("//div[@class='ffbzW _c']")
    	
    	for quadro in quadro_comentarios:
    		#item["autor_comentario"] = quadro.xpath(".").get()
    		item["autor_comentario"]  = quadro.xpath(".//span[@class='WlYyy cPsXC dTqpp']/a/text()" ).get()
    		item["autor_endereco"]    = quadro.xpath(".//div[@class='WlYyy diXIH bQCoY']/span/text()").get()
    		item["comentario_titulo"] = quadro.xpath(".//div[@class='WlYyy cPsXC bLFSo cspKb dTqpp']/a/span/text()").get()
    		item["comentario_corpo"]  = quadro.xpath(".//div[@class='WlYyy diXIH dDKKM']/span/text()").get()
    		item["comentario_data"]   = quadro.xpath(".//div[@class='WlYyy diXIH cspKb bQCoY']/text()").get()
    		yield item
    		
    		next_page = response.xpath(".//div[@class='cCnaz']/div/a/@href").get()
    		
    		if next_page:
    			yield response.follow( url = next_page, callback = self.parse )
    		
       
