import http.server
import socketserver
import webbrowser
import threading

PORT = 8080

HTML_APP = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>www.AshokOpticals.com | Official Optical Store & Lens Advisor - Indore</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #060911; color: #f8fafc; }
        .glass { background: rgba(15, 23, 42, 0.92); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); }
        .gold-btn { background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: #060911; font-weight: 800; }
        .blue-btn { background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); color: #ffffff; font-weight: 700; }
    </style>
</head>
<body class="min-h-screen pb-24">

    <!-- Browser URL Address Bar Display -->
    <div class="bg-black border-b border-slate-800 px-4 py-1.5 flex items-center justify-between text-xs">
        <div class="flex items-center gap-2 bg-slate-900 border border-slate-700 px-3 py-1 rounded-full text-emerald-400 font-mono">
            <i class="fa-solid fa-lock text-[10px]"></i>
            <span class="text-white font-bold">https://www.AshokOpticals.com</span>
            <span class="text-[10px] bg-emerald-500/20 text-emerald-300 px-1.5 rounded">Verified Official Store</span>
        </div>
        <span class="hidden sm:inline text-slate-400 text-[11px]">Pan-India Express Delivery | Old Palasia, Indore</span>
    </div>

    <!-- Store Info Strip -->
    <div class="bg-blue-950/90 border-b border-blue-800/50 text-blue-100 text-[11px] py-2 px-4">
        <div class="max-w-6xl mx-auto flex flex-wrap justify-between items-center gap-2">
            <span><i class="fa-solid fa-location-dot text-amber-400 mr-1"></i> Opp. Greater Kailash Hospital, Old Palasia, Indore, MP 452018 (Open till 9:30 PM)</span>
            <div class="flex items-center gap-3 font-bold">
                <span><i class="fa-solid fa-phone text-emerald-400 mr-1"></i> 099077 01540</span>
                <span class="bg-amber-500 text-slate-950 px-2 py-0.5 rounded text-[10px] font-black">DELIVERY ALL OVER INDIA</span>
            </div>
        </div>
    </div>

    <!-- Main Navigation Header -->
    <header class="sticky top-0 z-40 bg-slate-950/95 backdrop-blur border-b border-slate-800 px-4 py-3">
        <div class="max-w-6xl mx-auto flex justify-between items-center gap-2">
            <div class="flex items-center gap-2.5 cursor-pointer" onclick="app.showTab('home')">
                <div class="w-10 h-10 rounded-xl gold-btn flex items-center justify-center font-black text-base shadow-lg">AO</div>
                <div>
                    <div class="flex items-center gap-1.5">
                        <h1 class="font-black text-sm sm:text-base text-white tracking-wide">ASHOK OPTICALS</h1>
                        <span class="bg-emerald-500/20 text-emerald-300 text-[10px] font-bold px-2 py-0.5 rounded-full">4.8 ★ (697)</span>
                    </div>
                    <p class="text-[10px] text-slate-400">www.AshokOpticals.com • Ray-Ban • Titan • Crizal • Zeiss</p>
                </div>
            </div>

            <!-- Desktop Menu -->
            <nav class="hidden lg:flex items-center gap-5 text-xs font-bold text-slate-300">
                <button onclick="app.showTab('home')" class="hover:text-amber-400">Home</button>
                <button onclick="app.showTab('catalog')" class="hover:text-amber-400">Shop Catalog</button>
                <button onclick="app.showTab('calc')" class="hover:text-amber-400 text-amber-400"><i class="fa-solid fa-calculator mr-1"></i>Calculator</button>
                <button onclick="app.showTab('consult')" class="hover:text-amber-400 text-blue-400"><i class="fa-solid fa-comments mr-1"></i>Optician Chat</button>
                <button onclick="app.showTab('book')" class="hover:text-amber-400">Book Eye Test</button>
                <button onclick="app.showTab('track')" class="hover:text-amber-400">Track Order</button>
            </nav>

            <!-- Action Buttons -->
            <div class="flex items-center gap-2">
                <button onclick="app.openCart()" class="relative glass px-3 py-2 rounded-xl text-xs font-bold text-white hover:border-amber-400">
                    <i class="fa-solid fa-bag-shopping text-amber-400 mr-1"></i>
                    <span id="cartBadge">0</span>
                </button>
                <button onclick="app.openOwnerModal()" class="glass px-3 py-2 rounded-xl text-xs font-bold text-slate-200 hover:border-blue-400 flex items-center gap-1.5">
                    <i id="lockIcon" class="fa-solid fa-lock text-amber-400 text-[10px]"></i>
                    <span>Owner</span>
                </button>
            </div>
        </div>
    </header>

    <!-- MAIN CONTENT -->
    <main class="max-w-6xl mx-auto p-4 space-y-6">

        <!-- 1. HOME TAB -->
        <section id="tab-home" class="space-y-6">
            <div class="rounded-3xl p-6 md:p-10 bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900 border border-blue-500/30 shadow-2xl space-y-4">
                <span class="bg-amber-500/20 border border-amber-400/40 text-amber-300 px-3 py-1 rounded-full text-xs font-bold">★ 4.8 Rated Optician in Indore (697+ Google Reviews)</span>
                <h2 class="text-2xl md:text-4xl font-black text-white leading-tight">Precision Eyewear, Contact Lenses & Computerized Eye Testing</h2>
                <p class="text-xs md:text-sm text-slate-300 max-w-2xl">Shop authentic Ray-Ban, Titan, Fastrack, Crizal, Zeiss, and standalone Enterprise double-sided anti-reflective lenses with pan-India home delivery.</p>
                <div class="flex flex-wrap gap-2.5 pt-2">
                    <button onclick="app.showTab('catalog')" class="gold-btn px-5 py-3 rounded-xl text-xs shadow-lg">Shop Live Catalog</button>
                    <button onclick="app.showTab('calc')" class="blue-btn px-5 py-3 rounded-xl text-xs shadow-lg"><i class="fa-solid fa-calculator mr-1"></i> Price Calculator</button>
                    <button onclick="app.showTab('consult')" class="glass border-emerald-500/40 text-emerald-300 font-bold px-4 py-3 rounded-xl text-xs"><i class="fa-solid fa-user-doctor mr-1"></i> Live Optician Chat</button>
                    <button onclick="app.toggleChat()" class="glass border-blue-500/40 text-blue-300 font-bold px-4 py-3 rounded-xl text-xs"><i class="fa-solid fa-robot mr-1"></i> AI Lens Bot</button>
                </div>
            </div>

            <div class="flex justify-between items-center">
                <h3 class="font-extrabold text-base text-white">Available In-Stock Collection</h3>
                <button onclick="app.showTab('catalog')" class="text-amber-400 text-xs font-bold">View Full Catalog &rarr;</button>
            </div>
            <div id="homeGrid" class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4"></div>
        </section>

        <!-- 2. CATALOG TAB -->
        <section id="tab-catalog" class="hidden space-y-4">
            <div class="glass p-4 rounded-2xl flex flex-wrap justify-between items-center gap-3">
                <div>
                    <h2 class="text-lg font-extrabold text-white">Store Catalog & Uploaded PDFs</h2>
                    <p class="text-[11px] text-slate-400">Live inventory managed by Ashok Opticals</p>
                </div>
                <div class="flex gap-2 overflow-x-auto text-xs pb-1">
                    <button onclick="app.filterCat('All')" class="bg-blue-600 text-white px-3.5 py-2 rounded-xl font-bold">All</button>
                    <button onclick="app.filterCat('Spectacles')" class="glass text-slate-200 px-3.5 py-2 rounded-xl font-semibold">Spectacles</button>
                    <button onclick="app.filterCat('Sunglasses')" class="glass text-slate-200 px-3.5 py-2 rounded-xl font-semibold">Sunglasses</button>
                    <button onclick="app.filterCat('Optical Lenses')" class="glass text-slate-200 px-3.5 py-2 rounded-xl font-semibold">Optical Lenses</button>
                    <button onclick="app.filterCat('Contact Lenses')" class="glass text-slate-200 px-3.5 py-2 rounded-xl font-semibold">Contact Lenses</button>
                    <button onclick="app.filterCat('PDF Catalog')" class="glass text-amber-300 px-3.5 py-2 rounded-xl font-semibold">📄 PDF Catalogs</button>
                </div>
            </div>
            <div id="catalogGrid" class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4"></div>
        </section>

        <!-- 3. FULL CUSTOMER & STANDARD CALCULATOR TAB -->
        <section id="tab-calc" class="hidden grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Optical Package Estimator -->
            <div class="glass p-6 rounded-3xl space-y-4 border border-amber-500/30">
                <h3 class="font-black text-white text-base"><i class="fa-solid fa-glasses text-amber-400 mr-2"></i>Custom Spectacle & Lens Package Calculator</h3>
                <div class="space-y-3 text-xs">
                    <div>
                        <label class="block font-bold text-slate-300 mb-1">1. Lens Prescription Type:</label>
                        <select id="calcLens" onchange="app.calcPackage()" class="w-full bg-black text-white border border-slate-700 rounded-xl p-3 font-semibold">
                            <option value="600">Single Vision Lenses (₹600)</option>
                            <option value="1400">Bifocal Lenses (₹1,400)</option>
                            <option value="2800">Progressive Multifocal Lenses (₹2,800)</option>
                            <option value="1100">Monthly Contact Lenses Box (₹1,100)</option>
                        </select>
                    </div>
                    <div>
                        <label class="block font-bold text-slate-300 mb-1">2. Lens Brand & Coating:</label>
                        <select id="calcCoat" onchange="app.calcPackage()" class="w-full bg-black text-white border border-slate-700 rounded-xl p-3 font-semibold">
                            <option value="650">Enterprise Double-Sided AR + Smudge & Scratch Resistant (₹650)</option>
                            <option value="1500">Crizal Sapphire Anti-Glare Coating (₹1,500)</option>
                            <option value="2500">Zeiss Precision Pure Protection (₹2,500)</option>
                        </select>
                    </div>
                    <div>
                        <label class="block font-bold text-slate-300 mb-1">3. Frame Selection:</label>
                        <select id="calcFrame" onchange="app.calcPackage()" class="w-full bg-black text-white border border-slate-700 rounded-xl p-3 font-semibold">
                            <option value="0">No Frame - Lenses Only (₹0)</option>
                            <option value="1200">Fastrack / Standard Trendy Frame (₹1,200)</option>
                            <option value="2850">Titan Rimless / Metal Frame (₹2,850)</option>
                            <option value="6490">Ray-Ban Original Frame (₹6,490)</option>
                        </select>
                    </div>
                    <div class="bg-blue-950/70 p-4 rounded-2xl border border-blue-500/30 flex justify-between items-center">
                        <span class="font-bold text-white text-sm">Package Total:</span>
                        <span id="calcPkgTotal" class="font-black text-amber-400 text-xl">₹1,250</span>
                    </div>
                    <button onclick="app.addPkgToCart()" class="w-full gold-btn py-3.5 rounded-xl text-xs">Add Custom Package to Shopping Bag</button>
                </div>
            </div>

            <!-- Standard Math Calculator -->
            <div class="glass p-6 rounded-3xl space-y-4 border border-blue-500/30">
                <h3 class="font-black text-white text-base"><i class="fa-solid fa-calculator text-blue-400 mr-2"></i>Quick Math & Bill Calculator</h3>
                <input type="text" id="stdCalcDisplay" readonly placeholder="0" class="w-full bg-black text-white border border-slate-700 rounded-2xl p-4 text-right font-mono font-black text-2xl">
                <div class="grid grid-cols-4 gap-2 text-sm font-bold">
                    <button onclick="app.stdCalc('C')" class="bg-rose-600 text-white p-3.5 rounded-xl">C</button>
                    <button onclick="app.stdCalc('(')" class="bg-slate-800 text-white p-3.5 rounded-xl">(</button>
                    <button onclick="app.stdCalc(')')" class="bg-slate-800 text-white p-3.5 rounded-xl">)</button>
                    <button onclick="app.stdCalc('/')" class="bg-blue-600 text-white p-3.5 rounded-xl">÷</button>

                    <button onclick="app.stdCalc('7')" class="bg-slate-900 border border-slate-700 text-white p-3.5 rounded-xl">7</button>
                    <button onclick="app.stdCalc('8')" class="bg-slate-900 border border-slate-700 text-white p-3.5 rounded-xl">8</button>
                    <button onclick="app.stdCalc('9')" class="bg-slate-900 border border-slate-700 text-white p-3.5 rounded-xl">9</button>
                    <button onclick="app.stdCalc('*')" class="bg-blue-600 text-white p-3.5 rounded-xl">×</button>

                    <button onclick="app.stdCalc('4')" class="bg-slate-900 border border-slate-700 text-white p-3.5 rounded-xl">4</button>
                    <button onclick="app.stdCalc('5')" class="bg-slate-900 border border-slate-700 text-white p-3.5 rounded-xl">5</button>
                    <button onclick="app.stdCalc('6')" class="bg-slate-900 border border-slate-700 text-white p-3.5 rounded-xl">6</button>
                    <button onclick="app.stdCalc('-')" class="bg-blue-600 text-white p-3.5 rounded-xl">−</button>

                    <button onclick="app.stdCalc('1')" class="bg-slate-900 border border-slate-700 text-white p-3.5 rounded-xl">1</button>
                    <button onclick="app.stdCalc('2')" class="bg-slate-900 border border-slate-700 text-white p-3.5 rounded-xl">2</button>
                    <button onclick="app.stdCalc('3')" class="bg-slate-900 border border-slate-700 text-white p-3.5 rounded-xl">3</button>
                    <button onclick="app.stdCalc('+')" class="bg-blue-600 text-white p-3.5 rounded-xl">+</button>

                    <button onclick="app.stdCalc('0')" class="col-span-2 bg-slate-900 border border-slate-700 text-white p-3.5 rounded-xl">0</button>
                    <button onclick="app.stdCalc('.')" class="bg-slate-900 border border-slate-700 text-white p-3.5 rounded-xl">.</button>
                    <button onclick="app.stdCalc('=')" class="gold-btn p-3.5 rounded-xl">=</button>
                </div>
            </div>
        </section>

        <!-- 4. LIVE CUSTOMER-OWNER CONSULTATION CHAT -->
        <section id="tab-consult" class="hidden max-w-2xl mx-auto glass rounded-3xl overflow-hidden border border-blue-500/30">
            <div class="blue-btn p-4 flex justify-between items-center">
                <div>
                    <h3 class="font-extrabold text-sm">Direct Optician Consultation Chat</h3>
                    <p id="consultBannerText" class="text-[11px] text-amber-300 font-bold mt-0.5"></p>
                </div>
                <span class="bg-emerald-500 text-slate-950 text-[10px] font-black px-2.5 py-1 rounded-full">Owner Online</span>
            </div>
            <div id="consultMessages" class="p-4 h-80 overflow-y-auto bg-slate-950 space-y-2.5 text-xs"></div>
            <form onsubmit="app.sendConsultMsg(event)" class="p-3 bg-slate-900 border-t border-slate-800 flex gap-2">
                <input type="text" id="consultInput" required placeholder="Write your eye power or ask the shop owner..." class="flex-1 bg-black text-white border border-slate-700 rounded-xl px-3 py-2.5 text-xs">
                <button type="submit" class="gold-btn px-5 py-2.5 rounded-xl text-xs">Send</button>
            </form>
        </section>

        <!-- 5. BOOK EYE CHECKUP TAB -->
        <section id="tab-book" class="hidden max-w-md mx-auto glass p-6 rounded-3xl space-y-4">
            <h3 class="font-black text-white text-base text-center">Book Store Eye Checkup</h3>
            <p class="text-xs text-slate-400 text-center">Opp. Greater Kailash Hospital, Old Palasia, Indore</p>
            <form onsubmit="app.bookAppt(event)" class="space-y-3 text-xs">
                <input type="text" id="bName" required placeholder="Patient Full Name" class="w-full bg-black text-white border border-slate-700 rounded-xl p-3">
                <input type="tel" id="bPhone" required placeholder="10-Digit Mobile Number" class="w-full bg-black text-white border border-slate-700 rounded-xl p-3">
                <input type="date" id="bDate" required class="w-full bg-black text-white border border-slate-700 rounded-xl p-3">
                <select id="bTime" class="w-full bg-black text-white border border-slate-700 rounded-xl p-3">
                    <option>11:00 AM - 01:00 PM</option>
                    <option>04:00 PM - 06:30 PM</option>
                    <option>06:30 PM - 09:30 PM</option>
                </select>
                <button type="submit" class="w-full blue-btn py-3.5 rounded-xl">Confirm Appointment</button>
            </form>
            <div id="bookMsg" class="hidden p-3 bg-emerald-950 text-emerald-300 rounded-xl text-center text-xs font-bold">Appointment Booked Successfully!</div>
        </section>

        <!-- 6. TRACK ORDER TAB (Customer Only Sees Their Own Order) -->
        <section id="tab-track" class="hidden max-w-md mx-auto glass p-6 rounded-3xl space-y-4">
            <h3 class="font-black text-white text-base text-center">Track Your Order</h3>
            <p class="text-xs text-slate-400 text-center">Enter your unique Order ID (e.g. AO-1001)</p>
            <div class="flex gap-2">
                <input type="text" id="trackInput" placeholder="AO-XXXX" class="flex-1 bg-black text-white border border-slate-700 rounded-xl p-3 text-xs uppercase font-bold">
                <button onclick="app.trackOrder()" class="gold-btn px-5 py-3 rounded-xl text-xs">Track</button>
            </div>
            <div id="trackOutput" class="text-xs pt-2"></div>
        </section>

        <!-- 7. SECURE OWNER DASHBOARD -->
        <section id="tab-owner" class="hidden space-y-6">
            <div class="glass p-5 rounded-3xl flex flex-wrap justify-between items-center gap-3 border border-amber-500/40">
                <div>
                    <span class="bg-emerald-500/20 text-emerald-300 text-[10px] font-bold px-2.5 py-0.5 rounded-full">OWNER ADMIN PANEL UNLOCKED</span>
                    <h2 class="text-xl font-black text-white mt-1">www.AshokOpticals.com Control Center</h2>
                </div>
                <button onclick="app.lockOwner()" class="bg-rose-600 text-white px-4 py-2.5 rounded-xl text-xs font-bold"><i class="fa-solid fa-lock mr-1"></i> Lock Owner Panel</button>
            </div>

            <!-- Owner Profit Calculator & Settings Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <!-- Owner Business Profit Calculator -->
                <div class="glass p-4 rounded-2xl space-y-3 border border-emerald-500/30">
                    <h4 class="font-bold text-xs text-emerald-400"><i class="fa-solid fa-chart-line mr-1"></i> Owner Wholesale Profit & Margin Calculator</h4>
                    <div class="grid grid-cols-2 gap-2 text-xs">
                        <input type="number" id="owCost" placeholder="Wholesale Cost (₹)" oninput="app.calcOwnerProfit()" class="bg-black text-white border border-slate-700 rounded-xl p-2.5">
                        <input type="number" id="owMarkup" placeholder="Markup % (e.g. 50)" oninput="app.calcOwnerProfit()" class="bg-black text-white border border-slate-700 rounded-xl p-2.5">
                    </div>
                    <div class="bg-black p-3 rounded-xl border border-slate-800 flex justify-between text-xs font-bold">
                        <span>Selling Price: <b id="owSell" class="text-amber-400">₹0</b></span>
                        <span>Net Profit: <b id="owProfit" class="text-emerald-400">₹0</b></span>
                    </div>
                </div>

                <!-- Security PIN & Consultation Fee Settings -->
                <div class="glass p-4 rounded-2xl space-y-3 border border-indigo-500/30">
                    <h4 class="font-bold text-xs text-indigo-400"><i class="fa-solid fa-key mr-1"></i> Owner Security PIN & Consultation Fee</h4>
                    <form onsubmit="app.changePin(event)" class="flex gap-2 text-xs">
                        <input type="password" id="newPinInput" required minlength="4" maxlength="8" placeholder="Enter New Owner PIN" class="bg-black text-white border border-slate-700 rounded-xl p-2.5 flex-1 font-bold">
                        <button type="submit" class="blue-btn px-4 py-2.5 rounded-xl">Save PIN</button>
                    </form>
                    <div class="flex justify-between items-center pt-1 text-xs">
                        <span class="text-slate-300 font-semibold">Consultation Mode:</span>
                        <button onclick="app.toggleConsultFeeMode()" id="consultModeBtn" class="bg-emerald-600 text-white px-3 py-1.5 rounded-xl font-bold text-[11px]"></button>
                    </div>
                </div>
            </div>

            <!-- Add Product / Upload Specs Image or Lens Catalog PDF -->
            <div class="glass p-5 rounded-2xl space-y-3">
                <h4 class="font-bold text-xs text-amber-400"><i class="fa-solid fa-file-arrow-up mr-1"></i> Add Product / Upload Specs Image or Lens Catalog PDF</h4>
                <form onsubmit="app.addItem(event)" class="grid grid-cols-1 sm:grid-cols-4 gap-2.5 text-xs">
                    <input type="text" id="addName" required placeholder="Product / Catalog Title" class="bg-black text-white border border-slate-700 rounded-xl p-2.5">
                    <input type="text" id="addBrand" required placeholder="Brand (Ray-Ban/Zeiss/Enterprise)" class="bg-black text-white border border-slate-700 rounded-xl p-2.5">
                    <input type="number" id="addPrice" required placeholder="Price in ₹" class="bg-black text-white border border-slate-700 rounded-xl p-2.5">
                    <select id="addCat" class="bg-black text-white border border-slate-700 rounded-xl p-2.5">
                        <option>Spectacles</option>
                        <option>Sunglasses</option>
                        <option>Optical Lenses</option>
                        <option>Contact Lenses</option>
                        <option>PDF Catalog</option>
                    </select>
                    <div class="sm:col-span-3">
                        <input type="file" id="addFile" accept="image/*,.pdf" class="w-full bg-black text-white border border-slate-700 rounded-xl p-2 text-xs">
                    </div>
                    <button type="submit" class="gold-btn py-2.5 rounded-xl text-xs">Upload to Website</button>
                </form>
            </div>

            <!-- Live Inventory List (Stock Toggle + Remove Item) -->
            <div class="glass p-4 rounded-2xl space-y-3">
                <h4 class="font-bold text-xs text-white">Manage Store Inventory (Toggle Stock or Remove Item)</h4>
                <div id="ownerInvList" class="space-y-2 text-xs"></div>
            </div>

            <!-- All Customer Orders & Live Chat Reply -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="glass p-4 rounded-2xl space-y-2">
                    <h4 class="font-bold text-xs text-amber-400">Customer Orders</h4>
                    <div id="ownerOrderList" class="space-y-2 text-xs"></div>
                </div>
                <div class="glass p-4 rounded-2xl space-y-2">
                    <h4 class="font-bold text-xs text-blue-400">Reply to Customer Consultation Chat</h4>
                    <form onsubmit="app.ownerSendChat(event)" class="flex gap-2 text-xs">
                        <input type="text" id="ownerChatIn" required placeholder="Type reply to customer..." class="flex-1 bg-black text-white border border-slate-700 rounded-xl p-2.5">
                        <button type="submit" class="blue-btn px-4 rounded-xl">Reply</button>
                    </form>
                    <div id="ownerApptList" class="pt-3 space-y-1 text-xs text-slate-300"></div>
                </div>
            </div>
        </section>

    </main>

    <!-- FLOATING AI STOCK & LENS ADVISOR CHATBOT -->
    <button onclick="app.toggleChat()" class="fixed bottom-20 md:bottom-6 right-4 z-40 blue-btn p-3.5 rounded-2xl shadow-2xl flex items-center gap-2">
        <i class="fa-solid fa-robot text-base"></i>
        <span class="text-xs">AI Lens Advisor</span>
    </button>

    <div id="chatWidget" class="fixed bottom-36 md:bottom-20 right-4 z-50 w-80 glass rounded-3xl shadow-2xl border border-blue-500/40 hidden flex flex-col overflow-hidden">
        <div class="blue-btn p-3 flex justify-between items-center text-xs">
            <span>🤖 AI Live Stock & Lens Advisor</span>
            <button onclick="app.toggleChat()"><i class="fa-solid fa-xmark"></i></button>
        </div>
        <div id="aiMsgs" class="p-3 h-64 overflow-y-auto bg-slate-950 text-xs space-y-2">
            <div class="bg-slate-800 p-2.5 rounded-xl">Namaste! Ask me to recommend spectacles, sunglasses, or lenses based on our live store stock!</div>
        </div>
        <div class="px-2 py-1.5 bg-slate-900 border-t border-slate-800 flex gap-1 overflow-x-auto text-[10px]">
            <button onclick="app.quickAi('What is in stock right now?')" class="bg-slate-800 text-slate-200 px-2 py-1 rounded shrink-0">📦 Live Stock</button>
            <button onclick="app.quickAi('Recommend lenses')" class="bg-slate-800 text-slate-200 px-2 py-1 rounded shrink-0">👓 Best Lenses</button>
            <button onclick="app.quickAi('Show frames')" class="bg-slate-800 text-slate-200 px-2 py-1 rounded shrink-0">🕶️ Frames</button>
        </div>
        <form onsubmit="app.sendAiChat(event)" class="p-2 bg-slate-900 border-t border-slate-800 flex gap-2">
            <input type="text" id="aiIn" placeholder="Ask AI Advisor..." class="flex-1 bg-black text-white border border-slate-700 rounded-xl px-3 py-2 text-xs">
            <button type="submit" class="blue-btn px-3 py-2 rounded-xl text-xs">Send</button>
        </form>
    </div>

    <!-- OWNER PIN MODAL (Black Background, White Text, No Hint Shown) -->
    <div id="pinModal" class="fixed inset-0 z-50 bg-black/85 hidden flex items-center justify-center p-4">
        <div class="glass p-6 rounded-3xl text-center space-y-4 w-80 border border-slate-700">
            <i class="fa-solid fa-user-shield text-2xl text-amber-400"></i>
            <h3 class="font-black text-white text-base">Owner Security Verification</h3>
            <input type="password" id="pinBox" maxlength="8" placeholder="Enter PIN" class="w-full bg-black text-white border border-slate-600 rounded-xl p-3 text-center tracking-[0.4em] font-black text-lg outline-none">
            <div class="flex gap-2">
                <button onclick="document.getElementById('pinModal').classList.add('hidden')" class="flex-1 bg-slate-800 text-slate-300 py-2.5 rounded-xl text-xs font-bold">Cancel</button>
                <button onclick="app.verifyPin()" class="flex-1 gold-btn py-2.5 rounded-xl text-xs">Unlock</button>
            </div>
        </div>
    </div>

    <!-- CART & UPI CHECKOUT MODAL -->
    <div id="cartModal" class="fixed inset-0 z-50 bg-black/80 hidden flex justify-end">
        <div class="glass w-full max-w-sm h-full flex flex-col p-4 space-y-3">
            <div class="flex justify-between items-center border-b border-slate-800 pb-2 font-black text-sm">
                <span>Your Shopping Bag</span>
                <button onclick="app.closeCart()"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div id="cartList" class="flex-1 overflow-y-auto space-y-2 text-xs"></div>
            <div class="bg-blue-950/70 border border-blue-500/30 p-3 rounded-xl text-xs space-y-1">
                <p class="font-bold text-amber-400">Total Payable: <span id="cartTotal">₹0</span></p>
                <p class="text-[11px] text-slate-200">Pay via GPay / PhonePe / Paytm to Shop Number: <b class="text-emerald-400">09907701540</b></p>
            </div>
            <form onsubmit="app.placeOrder(event)" class="space-y-2 text-xs">
                <input type="text" id="oName" required placeholder="Your Full Name" class="w-full bg-black text-white border border-slate-700 rounded-xl p-2.5">
                <input type="tel" id="oPhone" required placeholder="Mobile Number" class="w-full bg-black text-white border border-slate-700 rounded-xl p-2.5">
                <input type="text" id="oUtr" required placeholder="UPI Ref / Last 4 Digits" class="w-full bg-black text-white border border-slate-700 rounded-xl p-2.5">
                <input type="text" id="oAddr" required placeholder="Full Delivery Address & Pincode" class="w-full bg-black text-white border border-slate-700 rounded-xl p-2.5">
                <input type="text" id="oPower" placeholder="Prescription Power / Coating Notes" class="w-full bg-black text-white border border-slate-700 rounded-xl p-2.5">
                <button type="submit" class="w-full gold-btn py-3 rounded-xl text-xs">Confirm UPI Payment & Place Order</button>
            </form>
        </div>
    </div>

    <!-- Mobile Bottom Bar -->
    <nav class="lg:hidden fixed bottom-0 left-0 right-0 bg-slate-950 border-t border-slate-800 z-30 flex justify-around py-2.5 text-[10px] font-bold text-slate-400">
        <button onclick="app.showTab('home')" class="flex flex-col items-center gap-1 text-amber-400"><i class="fa-solid fa-house"></i><span>Home</span></button>
        <button onclick="app.showTab('catalog')" class="flex flex-col items-center gap-1"><i class="fa-solid fa-glasses"></i><span>Catalog</span></button>
        <button onclick="app.showTab('calc')" class="flex flex-col items-center gap-1"><i class="fa-solid fa-calculator"></i><span>Calculator</span></button>
        <button onclick="app.showTab('consult')" class="flex flex-col items-center gap-1"><i class="fa-solid fa-comments"></i><span>Chat</span></button>
        <button onclick="app.showTab('track')" class="flex flex-col items-center gap-1"><i class="fa-solid fa-truck-fast"></i><span>Track</span></button>
    </nav>

    <script>
        const app = {
            products: JSON.parse(localStorage.getItem('ao_py_prod')) || [
                { id: 1, name: "Ray-Ban Aviator Classic Gold", cat: "Sunglasses", brand: "Ray-Ban", price: 6490, inStock: true, img: "https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=400&q=80", isPdf: false },
                { id: 2, name: "Titan Rimless Titanium Frame", cat: "Spectacles", brand: "Titan", price: 2850, inStock: true, img: "https://images.unsplash.com/photo-1591076482161-42ce6da69f67?w=400&q=80", isPdf: false },
                { id: 3, name: "Fastrack Matte Square Specs", cat: "Spectacles", brand: "Fastrack", price: 1599, inStock: true, img: "https://images.unsplash.com/photo-1508296695146-257a814070b4?w=400&q=80", isPdf: false },
                { id: 4, name: "Enterprise Standalone Double-AR Smudge-Proof Lenses", cat: "Optical Lenses", brand: "Enterprise", price: 1950, inStock: true, img: "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=400&q=80", isPdf: false },
                { id: 5, name: "Crizal Sapphire Anti-Glare Lenses", cat: "Optical Lenses", brand: "Crizal", price: 2200, inStock: true, img: "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=400&q=80", isPdf: false },
                { id: 6, name: "Zeiss Precision Pure Lenses", cat: "Optical Lenses", brand: "Zeiss", price: 3400, inStock: true, img: "https://images.unsplash.com/photo-1574258495973-f010dfbb5371?w=400&q=80", isPdf: false }
            ],
            cart: [],
            orders: JSON.parse(localStorage.getItem('ao_py_orders')) || [
                { id: "AO-1001", name: "Rajesh Verma", phone: "9826012345", utr: "UPI-4829", addr: "Old Palasia, Indore", power: "R:-1.50, L:-1.25", total: 2850, status: "In Lab / Fitting" }
            ],
            appts: JSON.parse(localStorage.getItem('ao_py_appts')) || [],
            chats: JSON.parse(localStorage.getItem('ao_py_chats')) || [
                { sender: "owner", text: "Namaste! Welcome to www.AshokOpticals.com live consultation. Ask about frame fit or lens prescriptions!" }
            ],
            ownerPin: localStorage.getItem('ao_py_pin') || "1234",
            consultFreeMode: true,
            unlocked: false,

            init() {
                this.renderStore();
                this.calcPackage();
                this.renderConsult();
            },

            showTab(t) {
                if(t === 'owner' && !this.unlocked) { this.openOwnerModal(); return; }
                ['home','catalog','calc','consult','book','track','owner'].forEach(id => {
                    document.getElementById('tab-' + id).classList.add('hidden');
                });
                document.getElementById('tab-' + t).classList.remove('hidden');
                if(t === 'owner') this.renderOwner();
            },

            renderStore() {
                const inStockItems = this.products.filter(p => p.inStock);
                document.getElementById('homeGrid').innerHTML = inStockItems.slice(0, 4).map(p => this.cardHtml(p)).join('');
                this.filterCat('All');
            },

            filterCat(cat) {
                const list = cat === 'All' ? this.products : this.products.filter(p => p.cat === cat);
                document.getElementById('catalogGrid').innerHTML = list.map(p => this.cardHtml(p)).join('');
            },

            cardHtml(p) {
                const media = p.isPdf
                    ? `<a href="${p.img}" download="${p.name}.pdf" class="w-full h-full bg-slate-900 flex flex-col items-center justify-center text-amber-400 p-2 text-center"><i class="fa-solid fa-file-pdf text-3xl mb-1"></i><span class="text-[10px] underline">Download PDF Catalog</span></a>`
                    : `<img src="${p.img}" class="w-full h-full object-cover ${p.inStock ? '' : 'grayscale opacity-40'}">`;

                const btn = p.inStock
                    ? `<button onclick="app.addCart(${p.id})" class="blue-btn text-[10px] px-3 py-1.5 rounded-lg">Add to Bag</button>`
                    : `<span class="text-[10px] text-rose-400 font-bold">Out of Stock</span>`;

                return `
                    <div class="glass rounded-2xl overflow-hidden flex flex-col justify-between">
                        <div>
                            <div class="h-36 bg-slate-900 relative">
                                ${media}
                                <span class="absolute top-2 left-2 bg-black/90 text-amber-400 text-[9px] font-bold px-2 py-0.5 rounded">${p.brand}</span>
                            </div>
                            <div class="p-3">
                                <p class="text-[10px] text-slate-400">${p.cat}</p>
                                <h4 class="font-bold text-xs text-white mt-0.5">${p.name}</h4>
                            </div>
                        </div>
                        <div class="p-3 pt-0 flex justify-between items-center border-t border-slate-800/80 mt-2">
                            <span class="font-black text-amber-400 text-xs">₹${p.price}</span>
                            ${btn}
                        </div>
                    </div>
                `;
            },

            // CALCULATORS
            calcPackage() {
                const l = Number(document.getElementById('calcLens').value);
                const c = Number(document.getElementById('calcCoat').value);
                const f = Number(document.getElementById('calcFrame').value);
                document.getElementById('calcPkgTotal').textContent = '₹' + (l + c + f);
            },

            addPkgToCart() {
                const l = Number(document.getElementById('calcLens').value);
                const c = Number(document.getElementById('calcCoat').value);
                const f = Number(document.getElementById('calcFrame').value);
                this.cart.push({ name: "Custom Optical Package", price: l + c + f });
                this.updateCart();
                this.openCart();
            },

            stdCalc(val) {
                const d = document.getElementById('stdCalcDisplay');
                if(val === 'C') d.value = '';
                else if(val === '=') {
                    try { d.value = eval(d.value) || 0; } catch { d.value = 'Error'; }
                } else { d.value += val; }
            },

            calcOwnerProfit() {
                const cost = Number(document.getElementById('owCost').value) || 0;
                const mark = Number(document.getElementById('owMarkup').value) || 0;
                const sell = Math.round(cost + (cost * mark / 100));
                document.getElementById('owSell').textContent = '₹' + sell;
                document.getElementById('owProfit').textContent = '₹' + (sell - cost);
            },

            // CART & ORDERS
            addCart(id) {
                const p = this.products.find(x => x.id === id);
                if(p && p.inStock) {
                    this.cart.push(p);
                    this.updateCart();
                    this.openCart();
                }
            },

            updateCart() {
                document.getElementById('cartBadge').textContent = this.cart.length;
                let total = 0;
                document.getElementById('cartList').innerHTML = this.cart.map((i, idx) => {
                    total += Number(i.price);
                    return `<div class="bg-slate-900 p-2.5 rounded-xl flex justify-between items-center"><span>${i.name}</span><div class="flex items-center gap-2"><b class="text-amber-400">₹${i.price}</b><button onclick="app.remCart(${idx})" class="text-rose-400">✕</button></div></div>`;
                }).join('') || '<p class="text-slate-500 text-center py-8">Bag is empty</p>';
                document.getElementById('cartTotal').textContent = '₹' + total;
                this.renderConsult();
            },

            remCart(idx) { this.cart.splice(idx, 1); this.updateCart(); },
            openCart() { this.updateCart(); document.getElementById('cartModal').classList.remove('hidden'); },
            closeCart() { document.getElementById('cartModal').classList.add('hidden'); },

            placeOrder(e) {
                e.preventDefault();
                if(this.cart.length === 0) { alert("Your bag is empty!"); return; }
                const id = "AO-" + Math.floor(1000 + Math.random() * 9000);
                const total = this.cart.reduce((s, i) => s + Number(i.price), 0);
                const ord = {
                    id,
                    name: document.getElementById('oName').value,
                    phone: document.getElementById('oPhone').value,
                    utr: document.getElementById('oUtr').value,
                    addr: document.getElementById('oAddr').value,
                    power: document.getElementById('oPower').value || "Standard",
                    total,
                    status: "Order Received"
                };
                this.orders.unshift(ord);
                localStorage.setItem('ao_py_orders', JSON.stringify(this.orders));
                this.cart = [];
                this.updateCart();
                this.closeCart();
                alert("Order Placed Successfully! Your Order Tracking ID is: " + id);
                document.getElementById('trackInput').value = id;
                this.showTab('track');
                this.trackOrder();
            },

            trackOrder() {
                const q = document.getElementById('trackInput').value.trim().toUpperCase();
                const o = this.orders.find(x => x.id === q);
                document.getElementById('trackOutput').innerHTML = o
                    ? `<div class="bg-slate-900 p-4 rounded-2xl border border-slate-700 space-y-1"><p class="font-black text-amber-400 text-sm">${o.id} — <span class="text-emerald-400">${o.status}</span></p><p class="text-white font-bold">${o.name} (${o.phone})</p><p class="text-slate-400">Address: ${o.addr}</p><p class="text-blue-300">Prescription: ${o.power}</p><p class="font-bold text-white pt-1">Paid via UPI: ₹${o.total}</p></div>`
                    : `<p class="text-rose-400 font-bold text-center">Order ID not found. Please check your Order ID.</p>`;
            },

            // CONSULTATION CHAT
            renderConsult() {
                const hasPurchase = this.cart.length > 0 || this.orders.length > 0;
                const banner = document.getElementById('consultBannerText');
                if(this.consultFreeMode || hasPurchase) {
                    banner.textContent = "Consultation Fee: FREE (100% Waived with Store Purchase)";
                } else {
                    banner.textContent = "Consultation Fee: ₹100 (Automatically FREE when you buy any item from store)";
                }
                const box = document.getElementById('consultMessages');
                box.innerHTML = this.chats.map(c => c.sender === 'owner'
                    ? `<div class="bg-slate-800 text-slate-100 p-3 rounded-2xl max-w-[85%]"><b class="text-amber-400 block text-[10px]">Ashok Opticals Owner:</b>${c.text}</div>`
                    : `<div class="bg-blue-600 text-white p-3 rounded-2xl ml-auto max-w-[85%]"><b class="text-blue-200 block text-[10px]">Customer:</b>${c.text}</div>`
                ).join('');
                box.scrollTop = box.scrollHeight;
            },

            sendConsultMsg(e) {
                e.preventDefault();
                const inp = document.getElementById('consultInput');
                if(!inp.value.trim()) return;
                this.chats.push({ sender: 'customer', text: inp.value.trim() });
                localStorage.setItem('ao_py_chats', JSON.stringify(this.chats));
                inp.value = '';
                this.renderConsult();
            },

            ownerSendChat(e) {
                e.preventDefault();
                const inp = document.getElementById('ownerChatIn');
                if(!inp.value.trim()) return;
                this.chats.push({ sender: 'owner', text: inp.value.trim() });
                localStorage.setItem('ao_py_chats', JSON.stringify(this.chats));
                inp.value = '';
                this.renderConsult();
                alert("Reply sent to customer chat!");
            },

            toggleConsultFeeMode() {
                this.consultFreeMode = !this.consultFreeMode;
                this.renderOwner();
                this.renderConsult();
            },

            // APPOINTMENTS
            bookAppt(e) {
                e.preventDefault();
                this.appts.unshift({
                    name: document.getElementById('bName').value,
                    phone: document.getElementById('bPhone').value,
                    date: document.getElementById('bDate').value,
                    time: document.getElementById('bTime').value
                });
                localStorage.setItem('ao_py_appts', JSON.stringify(this.appts));
                e.target.reset();
                document.getElementById('bookMsg').classList.remove('hidden');
            },

            // OWNER SECURITY & INVENTORY
            openOwnerModal() {
                if(this.unlocked) { this.showTab('owner'); return; }
                document.getElementById('pinBox').value = '';
                document.getElementById('pinModal').classList.remove('hidden');
            },

            verifyPin() {
                if(document.getElementById('pinBox').value === this.ownerPin) {
                    this.unlocked = true;
                    document.getElementById('pinModal').classList.add('hidden');
                    document.getElementById('lockIcon').className = "fa-solid fa-lock-open text-emerald-400 text-[10px]";
                    this.showTab('owner');
                } else {
                    alert("Access Denied: Incorrect Owner PIN!");
                }
            },

            lockOwner() {
                this.unlocked = false;
                document.getElementById('lockIcon').className = "fa-solid fa-lock text-amber-400 text-[10px]";
                this.showTab('home');
            },

            changePin(e) {
                e.preventDefault();
                const np = document.getElementById('newPinInput').value.trim();
                this.ownerPin = np;
                localStorage.setItem('ao_py_pin', np);
                document.getElementById('newPinInput').value = '';
                alert("Owner PIN changed successfully!");
            },

            addItem(e) {
                e.preventDefault();
                const fIn = document.getElementById('addFile');
                const save = (url, isPdf) => {
                    this.products.unshift({
                        id: Date.now(),
                        name: document.getElementById('addName').value,
                        brand: document.getElementById('addBrand').value,
                        price: Number(document.getElementById('addPrice').value),
                        cat: document.getElementById('addCat').value,
                        inStock: true,
                        img: url,
                        isPdf: isPdf
                    });
                    localStorage.setItem('ao_py_prod', JSON.stringify(this.products));
                    this.renderStore();
                    this.renderOwner();
                    e.target.reset();
                };

                if(fIn.files && fIn.files[0]) {
                    const file = fIn.files[0];
                    const isPdf = file.type === "application/pdf" || file.name.endsWith(".pdf");
                    const reader = new FileReader();
                    reader.onload = ev => save(ev.target.result, isPdf);
                    reader.readAsDataURL(file);
                } else {
                    save("https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=400&q=80", false);
                }
            },

            toggleStock(id) {
                const p = this.products.find(x => x.id === id);
                if(p) {
                    p.inStock = !p.inStock;
                    localStorage.setItem('ao_py_prod', JSON.stringify(this.products));
                    this.renderStore();
                    this.renderOwner();
                }
            },

            removeItem(id) {
                this.products = this.products.filter(x => x.id !== id);
                localStorage.setItem('ao_py_prod', JSON.stringify(this.products));
                this.renderStore();
                this.renderOwner();
            },

            updateOrderStatus(id, st) {
                const o = this.orders.find(x => x.id === id);
                if(o) {
                    o.status = st;
                    localStorage.setItem('ao_py_orders', JSON.stringify(this.orders));
                }
            },

            renderOwner() {
                document.getElementById('consultModeBtn').textContent = this.consultFreeMode
                    ? "Always FREE"
                    : "₹100 Fee (Free if Customer Buys)";

                document.getElementById('ownerInvList').innerHTML = this.products.map(p => `
                    <div class="bg-black p-2.5 rounded-xl border border-slate-800 flex justify-between items-center gap-2">
                        <span><b>${p.name}</b> (${p.brand} • ${p.cat}) — <b class="text-amber-400">₹${p.price}</b></span>
                        <div class="flex gap-1.5 shrink-0">
                            <button onclick="app.toggleStock(${p.id})" class="px-2.5 py-1 rounded-lg font-bold ${p.inStock ? 'bg-emerald-500/20 text-emerald-300' : 'bg-amber-500/20 text-amber-300'}">${p.inStock ? 'In Stock' : 'Out of Stock'}</button>
                            <button onclick="app.removeItem(${p.id})" class="bg-rose-600 text-white px-2.5 py-1 rounded-lg font-bold">Remove</button>
                        </div>
                    </div>
                `).join('');

                document.getElementById('ownerOrderList').innerHTML = this.orders.map(o => `
                    <div class="bg-black p-2.5 rounded-xl border border-slate-800 flex justify-between items-center">
                        <div>
                            <p class="font-bold text-amber-400">${o.id} — ${o.name} (${o.phone})</p>
                            <p class="text-[10px] text-slate-400">UPI: ${o.utr} | ₹${o.total} | Power: ${o.power}</p>
                        </div>
                        <select onchange="app.updateOrderStatus('${o.id}', this.value)" class="bg-slate-900 text-white border border-slate-700 rounded p-1 text-[10px]">
                            <option ${o.status==='Order Received'?'selected':''}>Order Received</option>
                            <option ${o.status==='In Lab / Fitting'?'selected':''}>In Lab / Fitting</option>
                            <option ${o.status==='Ready for Dispatch'?'selected':''}>Ready for Dispatch</option>
                            <option ${o.status==='Delivered'?'selected':''}>Delivered</option>
                        </select>
                    </div>
                `).join('');

                document.getElementById('ownerApptList').innerHTML = `<p class="font-bold text-white">Booked Eye Checkups (${this.appts.length}):</p>` +
                    this.appts.map(a => `<div class="bg-black p-2 rounded border border-slate-800">${a.name} (${a.phone}) — ${a.date} at ${a.time}</div>`).join('');
            },

            // AI STOCK-AWARE CHATBOT
            toggleChat() { document.getElementById('chatWidget').classList.toggle('hidden'); },
            quickAi(q) { document.getElementById('aiIn').value = q; this.sendAiChat(new Event('submit')); },

            sendAiChat(e) {
                e.preventDefault();
                const inp = document.getElementById('aiIn');
                const q = inp.value.trim();
                if(!q) return;
                inp.value = '';

                const box = document.getElementById('aiMsgs');
                box.innerHTML += `<div class="bg-blue-600 text-white p-2 rounded-xl ml-auto max-w-[82%]">${q}</div>`;

                const inStock = this.products.filter(p => p.inStock);
                const lenses = inStock.filter(p => p.cat === 'Optical Lenses' || p.cat === 'Contact Lenses');
                const frames = inStock.filter(p => p.cat === 'Spectacles' || p.cat === 'Sunglasses');
                const low = q.toLowerCase();

                let reply = "";
                if(low.includes("lens") || low.includes("coating") || low.includes("crizal") || low.includes("zeiss") || low.includes("enterprise")) {
                    reply = lenses.length > 0
                        ? `👓 <b>In-Stock Lenses Recommendation:</b> We have <b>${lenses.map(l => l.name + ' (₹' + l.price + ')').join(', ')}</b> ready in stock! For clear durability, choose our double-sided anti-reflective, smudge & scratch-resistant lenses.`
                        : `Currently all optical lenses are marked Out of Stock by the owner. Please check back soon!`;
                } else if(low.includes("frame") || low.includes("spec") || low.includes("sunglass") || low.includes("ray-ban") || low.includes("titan")) {
                    reply = frames.length > 0
                        ? `🕶️ <b>Available Frames in Stock:</b> You can order <b>${frames.map(f => f.name + ' (₹' + f.price + ')').join(', ')}</b> right now!`
                        : `Frames are currently out of stock.`;
                } else {
                    reply = `📦 <b>Live Store Stock (${inStock.length} items available):</b><br>` + inStock.map(p => `• <b>${p.name}</b> — ₹${p.price}`).join('<br>');
                }

                setTimeout(() => {
                    box.innerHTML += `<div class="bg-slate-800 text-slate-100 p-2.5 rounded-xl max-w-[88%]">${reply}</div>`;
                    box.scrollTop = box.scrollHeight;
                }, 200);
            }
        };

        window.addEventListener('DOMContentLoaded', () => app.init());
    </script>
</body>
</html>
"""

class AshokOpticalServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML_APP.encode("utf-8"))

    def log_message(self, format, *args):
        return  # Keeps console clean

def start_app():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), AshokOpticalServer) as httpd:
        url = f"http://localhost:{PORT}"
        print("======================================================")
        print("  www.AshokOpticals.com IS LIVE!")
        print(f"  Open in Browser: {url}")
        print("  Secret Default Owner PIN: 1234")
        print("======================================================")
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()
        httpd.serve_forever()

if __name__ == "__main__":
    start_app()
