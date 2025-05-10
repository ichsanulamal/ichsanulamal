# Scraping

npm i puppeteer


provide puppeteer script to scrape "https://www.enterkomputer.com/category_brand/17/processor/AMD". 
i want it to be output in objects/array like this

ps-product__title: AMD Ryzen Threadripper PRO 7995WX 2.5GHz Up To 5.1GHz Cache 384MB 350W sTR5 [BOX] - 96 Core - 100-100000884WOF
ps-product__title.href: https://www.enterkomputer.com/detail/186951/AMD-Ryzen-Threadripper-PRO-7995WX-25GHz-Up-To-51GHz-Cache-384MB-350W-sTR5-BOX-96-Core-100-100000884WOF
ps-product__price: Rp187.879.000

it has multi class 'ps-product ps-product--wide'.

this is the raw HTML: ```

<div class="ps-product ps-product--wide">
	<div class="ps-product__thumbnail img-zoomin">
		<img class="product-lazy" src="https://www.enterkomputer.com/assets/img/svg/noimage.svg" alt="image" style="">
	</div>
	<div class="ps-product__container">
		<div class="ps-product__content pe-2">
			<a class="ps-product__title"
				href="https://www.enterkomputer.com/detail/186951/AMD-Ryzen-Threadripper-PRO-7995WX-25GHz-Up-To-51GHz-Cache-384MB-350W-sTR5-BOX-96-Core-100-100000884WOF"
				aria-label="product-link" id="clipjs-186951">AMD Ryzen Threadripper PRO 7995WX 2.5GHz Up To 5.1GHz Cache
				384MB 350W sTR5 [BOX] - 96 Core - 100-100000884WOF</a>
			<div class="ps-product__act">
				<i class="fas fa-copy ms-2 clipjs" data-id="186951" data-clipboard-target="#clipjs-186951"></i>
				<i class="srch-img fab fa-google ms-2" data-id="186951"></i>
			</div>

			<span class="ps-sbadge badge--empty"></span>
			<div class="ps-product__sku"><i class="fas fa-barcode"></i> ZQBEZ23</div>

		</div>
		<div class="ps-product__shopping">
			<p class="ps-product__price">
				Rp187.879.000
				<span class="ps-product__price--down" rel="tooltip" title="harga turun Rp. 40.000"> 40.000</span>
			</p>
			<div class="ps-product__orders">
				<a href="#" target="_self" rel="nofollow,noopener" title="Whatsapp"
					class="btn-ico btn-ico--disabled btn-ico-wa whatsapp-orderbtn" data-shop=""></a>
			</div>
		</div>
	</div>
</div>
```