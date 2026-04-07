def seed_products(db):
    from models.product import Product

    if Product.query.count() > 0:
        return

    items = [
            # Electronics
        Product(name="Sony WH-1000XM5 Headphones", price=349.99, category="Electronics",
                description="Industry-leading noise canceling with 30-hour battery, multipoint connection, crystal-clear call quality. Foldable for portability. Perfect for travel and WFH.",
                tags="headphones audio wireless noise-canceling sony music",
                image_url="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&q=80"),

        Product(name="Apple AirPods Pro 2nd Gen", price=249.99, category="Electronics",
                description="Active Noise Cancellation, Transparency mode, Adaptive Audio. Up to 6 hours listening. H2 chip for unmatched sound. MagSafe charging case.",
                tags="airpods apple wireless earbuds audio noise-canceling",
                image_url="https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=500&q=80"),

        Product(name="Logitech MX Master 3S Mouse", price=99.99, category="Electronics",
                description="Ultra-fast MagSpeed electromagnetic scrolling, 8K DPI sensor tracks on any surface including glass. Connects up to 3 devices. Perfect for power users.",
                tags="mouse logitech wireless ergonomic productivity office",
                image_url="https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500&q=80"),

        Product(name="Samsung 27-inch 4K Monitor", price=429.99, category="Electronics",
                description="4K UHD IPS panel, 99% sRGB, HDR10, USB-C with 65W power delivery. Ultra-slim bezels. Ideal for designers and multitaskers who need colour accuracy.",
                tags="monitor samsung 4k display screen office creative",
                image_url="https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500&q=80"),

        Product(name="Anker 65W GaN USB-C Charger", price=35.99, category="Electronics",
                description="Compact 3-port GaN charger powers a laptop, tablet, and phone simultaneously. Folds flat for travel. Compatible with MacBook, iPad, iPhone, and Android.",
                tags="charger anker usb-c power laptop fast-charging travel",
                image_url="https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=500&q=80"),

        Product(name="Kindle Paperwhite 16GB", price=149.99, category="Electronics",
                description="Waterproof 6.8-inch glare-free display, adjustable warm light, 16GB storage for thousands of books. Single charge lasts up to 10 weeks. Only 205g.",
                tags="kindle ereader books reading amazon paperwhite waterproof",
                image_url="https://images.unsplash.com/photo-1592503254549-d83d24a4dfab?w=500&q=80"),

        # Home & Kitchen
        Product(name="Nespresso Vertuo Next", price=159.99, category="Home & Kitchen",
                description="Brew 5 coffee sizes from espresso to alto. Centrifusion technology reads capsule barcodes to auto-adjust brewing. WiFi connected for updates. Includes welcome kit.",
                tags="coffee nespresso espresso machine kitchen brew morning capsule",
                image_url="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=500&q=80"),

        Product(name="Instant Pot Duo 7-in-1 6Qt", price=89.99, category="Home & Kitchen",
                description="Pressure cooker, slow cooker, rice cooker, steamer, sauté pan, yogurt maker, and warmer. 13 smart programs. Saves up to 70% cooking time. Feeds 4-6 people.",
                tags="instant pot pressure cooker kitchen cooking meals family",
                image_url="https://images.unsplash.com/photo-1585515320310-259814833e62?w=500&q=80"),

        Product(name="Dyson V15 Detect Cordless Vacuum", price=699.99, category="Home & Kitchen",
                description="Laser reveals microscopic dust. Acoustic sensor counts and sizes particles live on-screen. 60-minute run time. HEPA filtration captures 99.99% of particles.",
                tags="dyson vacuum cleaner cordless home cleaning powerful laser",
                image_url="https://images.unsplash.com/photo-1558317374-067fb5f30001?w=500&q=80"),

        # Books & Stationery
        Product(name="Leuchtturm1917 A5 Hardcover Notebook", price=24.99, category="Books & Stationery",
                description="251 numbered pages, table of contents, ink-proof paper. Hardcover with elastic band, pen loop, two ribbon bookmarks. The gold standard for bullet journaling.",
                tags="notebook journal writing stationery leuchtturm bullet journal planner",
                image_url="https://images.unsplash.com/photo-1531346878377-a5be20888e57?w=500&q=80"),

        Product(name="Muji Gel Ink Pen Set 10pc", price=18.99, category="Books & Stationery",
                description="Smooth 0.5mm gel ink pens in 10 classic colours. Minimal Japanese design, comfortable grip, consistent ink flow with no skipping. Refillable.",
                tags="pens muji gel ink writing stationery office school",
                image_url="https://images.unsplash.com/photo-1585336261022-680e295ce3fe?w=500&q=80"),

        Product(name="Atomic Habits — James Clear", price=16.99, category="Books & Stationery",
                description="15 million copies sold. Practical, proven framework for building good habits and breaking bad ones. Based on how habits actually work in the human brain.",
                tags="book habits self-help productivity james clear bestseller",
                image_url="https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=500&q=80"),

        # Clothing
        Product(name="Uniqlo Ultra Light Down Jacket", price=79.99, category="Clothing",
                description="Incredibly light packable down jacket compresses into its own pocket. 90/10 down fill, DWR water-resistant coating. Available in 15 colours. Machine washable.",
                tags="jacket down uniqlo light packable winter warm clothing",
                image_url="https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=500&q=80"),

        Product(name="Levi's 501 Original Jeans", price=69.99, category="Clothing",
                description="The original blue jean since 1873. Straight leg, button fly, 5-pocket styling. 100% cotton denim that softens and molds to your body. A true wardrobe essential.",
                tags="jeans levis denim clothing casual fashion pants classic",
                image_url="https://images.unsplash.com/photo-1542272454315-4c01d7abdf4a?w=500&q=80"),

        Product(name="New Balance 574 Sneakers", price=89.99, category="Clothing",
                description="Iconic silhouette, suede and mesh upper. ENCAP midsole combines EVA foam for cushioning with polyurethane rim for support. Versatile for casual wear and light activity.",
                tags="sneakers shoes new balance casual comfort fashion sport",
                image_url="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&q=80"),

        # Health & Beauty
        Product(name="Theragun Mini Massager", price=179.99, category="Health & Beauty",
                description="Portable percussive therapy. 3 speeds up to 2400 PPM. 150-minute battery. Whisper quiet. Relieves muscle soreness and stiffness. Fits in any bag.",
                tags="massager theragun recovery muscle health fitness wellness percussive",
                image_url="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=500&q=80"),

        Product(name="CeraVe Moisturising Cream 19oz", price=19.99, category="Health & Beauty",
                description="Developed with dermatologists. Three essential ceramides restore the skin barrier. 24-hour hydration with hyaluronic acid. Non-comedogenic, fragrance-free. Face and body.",
                tags="moisturiser cerave skincare cream skin dry hydration beauty face",
                image_url="https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=500&q=80"),

        # Sports & Outdoors
        Product(name="Hydro Flask 32oz Water Bottle", price=44.99, category="Sports & Outdoors",
                description="TempShield vacuum insulation keeps drinks cold 24h, hot 12h. BPA-free 18/8 stainless steel. Wide mouth, powder-coat grip, dishwasher safe. Lifetime warranty.",
                tags="water bottle hydro flask insulated outdoor sports hiking",
                image_url="https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=500&q=80"),

        Product(name="Premium Yoga Mat 6mm", price=54.99, category="Sports & Outdoors",
                description="Extra-thick 6mm non-slip mat with alignment lines. Eco-friendly TPE, odorless, sweat-resistant. Includes carrying strap. 72x24 inches. For yoga, pilates, stretching.",
                tags="yoga mat exercise fitness sports workout pilates health stretching",
                image_url="https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=500&q=80"),

        Product(name="Peak Design 20L Everyday Backpack", price=279.99, category="Sports & Outdoors",
                description="Most versatile everyday carry backpack. FlexFold dividers adapt for camera gear or clothes. MagLatch top closure. Weatherproof 400D nylon. Padded 16-inch laptop sleeve.",
                tags="backpack peak design camera bag laptop everyday carry travel",
                image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500&q=80"),

        # ── More Electronics ──────────────────────────────────
        Product(name="Raspberry Pi 5 (8GB)", price=80.00, category="Electronics",
                description="The most powerful Raspberry Pi yet. Quad-core 64-bit Arm Cortex-A76 processor running at 2.4GHz. Dual 4K display output, PCIe connector, and improved I/O. Perfect for makers, hobbyists, and developers.",
                tags="raspberry pi maker coding diy electronics single board computer",
                image_url="https://images.unsplash.com/photo-1601132359864-c974e79890ac?w=500&q=80"),

        Product(name="GoPro HERO12 Black", price=399.99, category="Electronics",
                description="5.3K60 video, 27MP photos, HyperSmooth 6.0 stabilization. Waterproof to 10m without a case. 2-hour battery life. Works with all GoPro mounts. Ideal for action sports, travel, and vlogging.",
                tags="gopro camera action waterproof video travel sport vlog",
                image_url="https://images.unsplash.com/photo-1519458246479-da7e16800d7b?w=500&q=80"),

        Product(name="Elgato Stream Deck MK.2", price=149.99, category="Electronics",
                description="15 customisable LCD keys for instant control of streaming, editing, and productivity. Works with OBS, Twitch, YouTube, Spotify, and more. Fully programmable with drag-and-drop actions. USB-C connection.",
                tags="stream deck elgato streaming twitch youtube content creator obs",
                image_url="https://images.unsplash.com/photo-1593640408182-31c228f60b9d?w=500&q=80"),

        Product(name="Rode NT-USB Mini Microphone", price=99.00, category="Electronics",
                description="Studio-quality USB condenser microphone for podcasting, streaming, and remote work. Cardioid pickup pattern, built-in pop filter, real-time headphone monitoring. Plug-and-play on Mac and PC.",
                tags="microphone rode podcast streaming recording usb condenser audio",
                image_url="https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=500&q=80"),

        Product(name="Tile Pro Bluetooth Tracker", price=34.99, category="Electronics",
                description="Find your keys, wallet, or bag in seconds. 400ft Bluetooth range, loud 105dB ring, water-resistant. Works with Alexa and Google Assistant. 1-year replaceable battery. Compatible with iOS and Android.",
                tags="tile tracker bluetooth keys wallet find lost item smart",
                image_url="https://images.unsplash.com/photo-1625895197185-efcec01cffe0?w=500&q=80"),

        # ── More Home & Kitchen ───────────────────────────────
        Product(name="Philips Hue Starter Kit (4 bulbs)", price=199.99, category="Home & Kitchen",
                description="Transform your home with 16 million colours and warm-to-cool white light. Works with Alexa, Google Home, and Apple HomeKit. Schedule, automate, and control from anywhere with the Hue app. Easy E27 fitting.",
                tags="philips hue smart light bulb colour home automation alexa",
                image_url="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500&q=80"),

        Product(name="Vitamix E310 Explorian Blender", price=349.95, category="Home & Kitchen",
                description="Variable speed control and pulse feature for total blending versatility. 48oz container ideal for small to medium batches. Aircraft-grade stainless steel blades. Self-cleaning in 30-60 seconds. 5-year warranty.",
                tags="blender vitamix smoothie kitchen powerful food prep healthy",
                image_url="https://images.unsplash.com/photo-1570222094114-d054a817e56b?w=500&q=80"),

        Product(name="Lodge Cast Iron Skillet 12-inch", price=44.90, category="Home & Kitchen",
                description="Pre-seasoned with natural oil for a natural easy-release finish. Works on all cooking surfaces — induction, oven, campfire. Retains heat evenly for perfect searing. Lasts generations with proper care.",
                tags="cast iron skillet lodge cooking pan kitchen frying sear oven",
                image_url="https://images.unsplash.com/photo-1590301157890-4810ed352733?w=500&q=80"),

        Product(name="Bamboo Cutting Board Set (3pc)", price=29.99, category="Home & Kitchen",
                description="Three sizes for every kitchen task. Eco-friendly bamboo is harder than maple and gentler on knife edges. Juice groove around the edges catches liquids. Dishwasher safe. Non-slip rubber feet.",
                tags="cutting board bamboo kitchen cooking eco knife chopping",
                image_url="https://images.unsplash.com/photo-1591261730799-ee4e6c2d16d7?w=500&q=80"),

        # ── More Clothing ─────────────────────────────────────
        Product(name="Patagonia Better Sweater Fleece", price=139.00, category="Clothing",
                description="Classic fleece with sweater-like appearance. Made from 100% recycled polyester fleece. Full-zip with zippered hand pockets and chest pocket. Relaxed fit. Ideal layering piece for outdoor adventures.",
                tags="patagonia fleece jacket recycled outdoor layer warm clothing",
                image_url="https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=500&q=80"),

        Product(name="Merino Wool Crew Neck Sweater", price=89.99, category="Clothing",
                description="Superfine 18.5 micron merino wool — incredibly soft, naturally odour-resistant, and temperature-regulating. Relaxed fit, ribbed cuffs and hem. Machine washable. Available in 12 colours.",
                tags="merino wool sweater soft warm clothing winter natural odour-free",
                image_url="https://images.unsplash.com/photo-1578587018452-892bacefd3f2?w=500&q=80"),

        Product(name="Arc'teryx Atom LT Hoody", price=259.00, category="Clothing",
                description="Lightweight insulated jacket with Coreloft Compact synthetic insulation. Trim fit designed for active use under a shell or as a standalone. Wind and moisture resistant. Packable into its own pocket.",
                tags="arcteryx jacket insulated hoody outdoor hiking lightweight packable",
                image_url="https://images.unsplash.com/photo-1604644401890-0bd678c83788?w=500&q=80"),

        Product(name="Stance Uncommon Solids Socks 5-Pack", price=55.00, category="Clothing",
                description="Premium combed cotton blend socks with reinforced heel and toe for durability. Arch support band reduces fatigue. Seamless toe closure. Five classic colours per pack. Everyday comfort engineered for all-day wear.",
                tags="socks stance comfort cotton everyday clothing accessories pack",
                image_url="https://images.unsplash.com/photo-1586350977771-b3b0abd50c82?w=500&q=80"),

        # ── More Health & Beauty ──────────────────────────────
        Product(name="Fitbit Charge 6", price=159.95, category="Health & Beauty",
                description="Built-in GPS, heart rate tracking, sleep scoring, stress management score, and ECG app. 7-day battery. Works with Google Maps, Wallet, and YouTube Music. Water-resistant to 50m. Compatible with Android and iOS.",
                tags="fitbit fitness tracker health heart rate sleep gps wearable",
                image_url="https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?w=500&q=80"),

        Product(name="Oral-B iO Series 7 Electric Toothbrush", price=149.99, category="Health & Beauty",
                description="Magnetic drive technology delivers up to 100% more plaque removal vs manual. Smart pressure sensor prevents brushing too hard. AI recognition identifies brushing style. 5 modes. Includes travel case.",
                tags="toothbrush oral-b electric dental health smart teeth whitening",
                image_url="https://images.unsplash.com/photo-1559591937-abc89e6555b1?w=500&q=80"),

        Product(name="The Ordinary Skincare Starter Set", price=39.90, category="Health & Beauty",
                description="Five hero products: Hyaluronic Acid 2% + B5, Niacinamide 10% + Zinc, AHA 30% + BHA 2%, Retinol 0.5%, and Squalane. Clinically proven formulas at accessible prices. Suitable for all skin types.",
                tags="the ordinary skincare routine serum retinol hyaluronic acid beauty",
                image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=500&q=80"),

        # ── More Sports & Outdoors ────────────────────────────
        Product(name="Garmin Forerunner 255 GPS Watch", price=349.99, category="Sports & Outdoors",
                description="Advanced running dynamics, training readiness score, race predictor, and HRV status. 14-day battery in smartwatch mode. Lightweight at 49g. Tracks over 30 sports. Sleep tracking and stress monitoring included.",
                tags="garmin gps watch running sport fitness triathlon heart rate outdoor",
                image_url="https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=500&q=80"),

        Product(name="TRX HOME2 Suspension Trainer", price=199.95, category="Sports & Outdoors",
                description="Full-body workout anywhere — door, tree, or post. Over 300 exercises using your own bodyweight. Military-grade nylon straps support up to 350kg. Includes door anchor, mesh bag, and workout guide.",
                tags="trx suspension trainer home gym workout fitness bodyweight exercise",
                image_url="https://images.unsplash.com/photo-1598289431512-b97b0917affc?w=500&q=80"),

        Product(name="Coleman Sundome 4-Person Tent", price=89.99, category="Sports & Outdoors",
                description="Easy 10-minute setup with continuous pole sleeves. WeatherTec system with patented welded floors and inverted seams keeps water out. Large windows and ground vent for airflow. Fits 2 queen airbeds.",
                tags="tent camping coleman outdoor shelter hiking 4 person weather",
                image_url="https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=500&q=80"),

        # ── Books & Stationery extras ─────────────────────────
        Product(name="The Psychology of Money — Morgan Housel", price=14.99, category="Books & Stationery",
                description="19 short stories exploring the strange ways people think about money. Timeless lessons on wealth, greed, and happiness. Over 4 million copies sold. Essential reading for anyone trying to make smarter financial decisions.",
                tags="book money finance psychology investing wealth morgan housel bestseller",
                image_url="https://images.unsplash.com/photo-1553729459-efe14ef6055d?w=500&q=80"),

        Product(name="Faber-Castell Watercolour Pencils 48pc", price=32.99, category="Books & Stationery",
                description="48 vibrant watercolour pencils that can be used dry or blended with water for painterly effects. Thick 3.8mm core resists breakage. Ideal for sketching, illustration, and adult colouring. Tin case included.",
                tags="pencils watercolour art drawing creative faber castell colouring sketch",
                image_url="https://images.unsplash.com/photo-1513364776144-60967b0f800f?w=500&q=80"),
                
                ]

    db.session.bulk_save_objects(items)
    db.session.commit()
    print(f"✅ Seeded {len(items)} products.")
