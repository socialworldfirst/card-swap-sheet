#!/usr/bin/env python3
"""Card boost swap sheet — wf-gated GH Pages page with per-ad copy buttons."""
import os, base64, json
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes

PASSWORD = "wf"
ITERATIONS = 100_000

def encrypt_payload(plaintext, password=PASSWORD):
    salt, iv = os.urandom(16), os.urandom(12)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITERATIONS)
    key = kdf.derive(password.encode())
    ct = AESGCM(key).encrypt(iv, plaintext.encode(), None)
    return {"v":1,"salt":base64.b64encode(salt).decode(),"iv":base64.b64encode(iv).decode(),
            "iterations":ITERATIONS,"ciphertext":base64.b64encode(ct).decode()}

U = "utm_medium=boosted&utm_campaign=card_awareness_jul26"
def url(lp, src, code): return f"{lp}?utm_source={src}&{U}&utm_content={code}"
UKLP = "https://www.worldfirst.com/uk/product/pay/world-card/"
MYLP = "https://www.worldfirst.com/my/"
EELP = "https://www.worldfirst.com/"

ROWS = [
 ("UK · campaign 120251291102340127", [
  ("BST_UK_TutorialVideo_IG_300","IG post","https://www.instagram.com/reel/DUiAbSiDB5s/",url(UKLP,"instagram","uk_tutorial_ig")),
    ("BST_UK_Carousel_IG_2000","IG post","https://www.instagram.com/p/DIOeAzkvVXX/",url(UKLP,"instagram","uk_carousel_ig")),
  ("BST_UK_Carousel_FB_1500","FB search: one card for all business expenses","",url(UKLP,"facebook","uk_carousel_fb")),
 ]),
 ("UK additions (2026-07-13) · same campaign 120251291102340127", [
  ("BST_UK_Slides2_IG_600","IG post","https://www.instagram.com/p/DIJJOB4RdRx/",url(UKLP,"instagram","uk_slides2_ig")),
  ("BST_UK_Slides2_FB_400","FB post (either): facebook.com/share/p/194rZqeC3d or /share/p/1Cn3vRS1cx","",url(UKLP,"facebook","uk_slides2_fb")),
  ("BST_UK_JimVideo_IG_900","IG post","https://www.instagram.com/reel/DKyjeu6NkHf/",url(UKLP,"instagram","uk_jimvideo_ig")),
   ]),
 ("MY · campaign 120251291108740127", [
  ("BST_MY_Coffee50k_IG_1200","IG post","https://www.instagram.com/reel/DZkBDcWEVyx/",url(MYLP,"instagram","my_coffee50k_ig")),
  ("BST_MY_Coffee50k_FB_800","FB search: spend can pay you back","",url(MYLP,"facebook","my_coffee50k_fb")),
  ("BST_MY_Dinner80_IG_1050","IG post","https://www.instagram.com/reel/DZuVA7-DXoU/",url(MYLP,"instagram","my_dinner80_ig")),
  ("BST_MY_Dinner80_FB_700","FB search: cashback is cute","",url(MYLP,"facebook","my_dinner80_fb")),
  ("BST_MY_SpendGrowth_IG_750","IG post","https://www.instagram.com/reel/DZ4oYkACgOP/",url(MYLP,"instagram","my_spendgrowth_ig")),
  ("BST_MY_SpendGrowth_FB_500","FB search: earning its keep","",url(MYLP,"facebook","my_spendgrowth_fb")),
 ]),
 ("EEA · campaign 120251291110050127", [
  (f"BST_EEA_{cc}_{cr}_{pl}_{b}",
   "IG post" if pl=="IG" else ("FB search: global business spend together" if cr=="Tutorial" else "FB search: one card for all business expenses"),
   ("https://www.instagram.com/reel/DUiAbSiDB5s/" if cr=="Tutorial" else "https://www.instagram.com/p/DIOeAzkvVXX/") if pl=="IG" else "",
   url(EELP, "instagram" if pl=="IG" else "facebook", f"{cc.lower()}_{cr.lower()}_{pl.lower()}"))
  for cc, sets in [("DE",[("Tutorial","IG",300),("Tutorial","FB",200),("Carousel","IG",600),("Carousel","FB",400)]),
                   ("NL",[("Tutorial","IG",300),("Tutorial","FB",200),("Carousel","IG",300),("Carousel","FB",200)]),
                   ("PL",[("Tutorial","IG",300),("Tutorial","FB",200),("Carousel","IG",300),("Carousel","FB",200)])]
  for cr, pl, b in sets
 ]),
 ("SG · campaign 120251291106820127 · builds after SG advertiser verification", [
  ("BST_SG_PointsFrozen_IG_1800 (planned)","IG post","https://www.instagram.com/reel/DV0bifviEc7/",url("https://www.worldfirst.com/sg/","instagram","sg_pointsfrozen_ig")),
  ("BST_SG_PointsFrozen_FB_1200 (planned)","FB search: points getting frozen","",url("https://www.worldfirst.com/sg/","facebook","sg_pointsfrozen_fb")),
  ("BST_SG_CorpCardSG_IG_1200 (planned)","IG post","https://www.instagram.com/reel/DXjMrRGvROV/",url("https://www.worldfirst.com/sg/","instagram","sg_corpcard_ig")),
  ("BST_SG_CorpCardSG_FB_800 (planned)","FB search: best corporate cards for Singapore","",url("https://www.worldfirst.com/sg/","facebook","sg_corpcard_fb")),
 ]),
]

DARK_POST = """<h2>Dark post spec &middot; BST_UK_Slides2_IG_600 &middot; 5-card carousel</h2>
<p class="sw-lead">IG dark post, 5 cards in THIS order (untick "show best performing cards first", the hero stays card 1). All images 1:1 1080&times;1080. Same CTA + URL on every card; Meta reports per-card pull on its own breakdown.</p>
<table>
<tr><th style="width:210px">Card</th><th>Headline</th><th>Description</th></tr>
<tr><td class="sw-n">1 &middot; hero "Save on Every Spend, Everywhere"</td><td>The business card that pays you back</td><td>Cashback on eligible spend. Free to get.</td></tr>
<tr><td class="sw-n">2 &middot; Marketing &amp; Advertising Fees</td><td>Your ad spend, earning back</td><td>Meta, Google and Amazon ads without the FX sting.</td></tr>
<tr><td class="sw-n">3 &middot; Software Subscriptions</td><td>Your SaaS stack, minus FX fees</td><td>Pay tools in their own currency, earn cashback.</td></tr>
<tr><td class="sw-n">4 &middot; Shipping &amp; Logistics Costs</td><td>Earn back on every shipment</td><td>Forwarders, freight and last-mile spend that returns.</td></tr>
<tr><td class="sw-n">5 &middot; Seller Store Fees</td><td>Marketplace fees, working for you</td><td>Amazon, Shopify, TikTok Shop and more.</td></tr>
</table>
<table>
<tr><th style="width:130px">Field</th><th>Use (all cards)</th></tr>
<tr><td class="sw-n">Primary text</td><td>Your business spends every day. World Card gives some of it back: cashback on eligible spend, and no FX fees on international payments. Free with your World Account.</td></tr>
<tr><td class="sw-n">CTA</td><td>Learn More</td></tr>
<tr><td class="sw-n">Website URL</td><td><code>https://www.worldfirst.com/uk/product/pay/world-card/?utm_source=instagram&utm_medium=boosted&utm_campaign=card_awareness_jul26&utm_content=uk_slides2_ig</code> <button class="sw-c" data-u="https://www.worldfirst.com/uk/product/pay/world-card/?utm_source=instagram&utm_medium=boosted&utm_campaign=card_awareness_jul26&utm_content=uk_slides2_fb" onclick="navigator.clipboard.writeText(this.dataset.u.replace('_fb','_ig'));this.textContent='copied';setTimeout(()=>this.textContent='copy URL',1200)">copy URL</button></td></tr>
<tr><td class="sw-n">Identity</td><td>WorldFirst page + @worldfirst Instagram</td></tr>
<tr><td class="sw-n">Tracking</td><td>Website pixel ON (LPV optimisation needs it)</td></tr>
</table>
<h2>Dark post carousel SET 2 &middot; purple Mastercard series &middot; 4 cards</h2>
<p class="sw-lead">Second World Card carousel (the FB share-link posts / purple design). Card 1 is portrait: crop 1:1 so the set matches. Same CTA + platform URL as the ad set it goes into.</p>
<table>
<tr><th style="width:210px">Card</th><th>Headline</th><th>Description</th></tr>
<tr><td class="sw-n">1 &middot; "Now Available Worldwide"</td><td>Free with your World Account</td><td>A WorldFirst and Mastercard business card.</td></tr>
<tr><td class="sw-n">2 &middot; "Save Big with Cashback"</td><td>Every purchase gives back</td><td>Cashback rates vary by region. T&amp;Cs apply.</td></tr>
<tr><td class="sw-n">3 &middot; "One Card for All Business Expenses"</td><td>Ads, freight and fees: one card</td><td>Separate cards per budget, one dashboard.</td></tr>
<tr><td class="sw-n">4 &middot; "Extensive Currencies, Effortless Savings"</td><td>Zero FX fees in 15 currencies</td><td>Spend in 150+ currencies across 210+ countries.</td></tr>
</table>
<table><tr><th style="width:130px">Field</th><th>Use (all cards)</th></tr>
<tr><td class="sw-n">Primary text</td><td>World Card is now available worldwide. A WorldFirst and Mastercard business card: cashback on eligible purchases, zero FX fees when paying in 15 major currencies from your account balance, accepted wherever Mastercard is.</td></tr>
<tr><td class="sw-n">CTA + URL</td><td>Learn More + the ad set's UTM URL from the tables above (ig / fb code per platform)</td></tr></table>
<p class="sw-lead">Copy notes: headlines add the mechanism, they never repeat the image text; "eligible spend" keeps cashback safe until the UK offer-wording check clears. FB Slides2 dark post: same 5 cards + copy, swap the URL utm_content to uk_slides2_fb and utm_source to facebook.</p>"""

FB_DARK = """<h2>FB dark ad specs &middot; per creative</h2>
<p class="sw-lead">FB "use existing post" cannot attach a proper CTA button + website URL (only link-posts can), so every FB ad set runs as a DARK POST: upload the same media, primary text below (reworked from the organic caption), headline + description, CTA <b>Learn More</b>, and the ad set's UTM URL from the tables above. Pixel ON everywhere.</p>
<table>
<tr><th style="width:190px">Creative (FB ad sets)</th><th>Primary text</th><th>Headline</th><th>Description</th></tr>
<tr><td class="sw-n">Tutorial video<br>(UK + DE/NL/PL)</td><td>Paying in different currencies across markets? World Card brings your business spend into one place: ads, logistics, subscriptions and marketplace fees, with cashback on eligible purchases. Free with your World Account.</td><td>Get your World Card free</td><td>Apply in minutes from your World Account.</td></tr>
<tr><td class="sw-n">Intro carousel DIOeAzkvVXX<br>(UK + DE/NL/PL)</td><td>Running a global business can be challenging and costly, but it doesn't have to be. Meet World Card: one card for all business expenses, from marketing and advertising to software, seller store fees, shipping and logistics.</td><td>One card for all business expenses</td><td>Cashback on eligible spend. Free to get.</td></tr>
<tr><td class="sw-n">Slides2 carousel (UK)</td><td colspan="3">Use the 5-card carousel spec above, swap URL utm_source to facebook and utm_content to uk_slides2_fb.</td></tr>
<tr><td class="sw-n">Jim Vrondas video (UK)</td><td>Jim Vrondas on how World Card gives online sellers faster access to global funds and more control over business spend.</td><td>Hear why sellers use World Card</td><td>Cashback on eligible spend, no FX fees.</td></tr>
<tr><td class="sw-n">Coffee vs $50k (MY)</td><td>Your business spend can pay you back. Suppliers, restocks, ads: you're spending thousands anyway. World Card gives you cashback on that spend.</td><td>Cashback on business spend</td><td>Check your Malaysia rate.</td></tr>
<tr><td class="sw-n">$80 dinner (MY)</td><td>Personal cashback is cute. This one counts. Supplier invoices, ad spend, flights: put them on a card that pays you back.</td><td>Business cashback that counts</td><td>See your Malaysia rate.</td></tr>
<tr><td class="sw-n">Spend funds growth (MY)</td><td>Every expense your business makes could be earning its keep. Stock, software, suppliers, travel: the same spend, finally pulling its weight.</td><td>Let your spend earn its keep</td><td>See what World Card pays back.</td></tr>
</table>
<p class="sw-lead">Video files: pull the same cuts used for the IG posts (Frame.io / original renders). The IG ad sets stay "use existing post", IG supports CTA + URL on existing posts fine.</p>"""

sections = ""
for title, rows in ROWS:
    trs = ""
    for name, how, post, u in rows:
        post_cell = f'<a href="{post}" target="_blank" rel="noopener">{post.split("/")[-2]}</a>' if post else f'<em>{how}</em>'
        trs += (f'<tr><td class="sw-n">{name}</td><td>{post_cell}</td>'
                f'<td class="sw-u"><code>{u}</code></td>'
                f'<td><button class="sw-c" data-u="{u}" onclick="navigator.clipboard.writeText(this.dataset.u);this.textContent=\'copied\';setTimeout(()=>this.textContent=\'copy URL\',1200)">copy URL</button></td></tr>')
    sections += f'<h2>{title}</h2><table><tr><th>Ad set</th><th>Post</th><th>Website URL (CTA = Learn More)</th><th></th></tr>{trs}</table>'

inner = f"""<div class="sw-wrap"><h1>Card boosts · swap sheet</h1>
<p class="sw-lead">Per ad set: open the ad, "use existing post" (IG via link, FB via the search phrase), set CTA to <b>Learn More</b>, paste the Website URL, delete the zzPLACEHOLDER ad. All campaigns PAUSED until activation. Envelope US$25,000 to 31 Jul.</p>
{sections}\n{DARK_POST}
{FB_DARK}
<p class="sw-foot">MY + EEA URLs point at regional homepages until card LPs are confirmed. <a href="#" onclick="localStorage.removeItem('card_swap_pw');location.reload();return false;">lock device</a></p></div>"""

payload_json = json.dumps(encrypt_payload(inner))
html = """<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>swap sheet</title>
<style>
body{font:14px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:#111;margin:0;padding:28px 18px}
.sw-wrap{max-width:1080px;margin:0 auto}h1{font-size:20px}h2{font-size:14px;margin:26px 0 6px}
.sw-lead,.sw-foot{color:#666;font-size:13px}table{border-collapse:collapse;width:100%;font-size:12.5px}
td,th{border-bottom:1px solid #ececec;padding:6px 8px;text-align:left;vertical-align:top}
th{color:#888;font-size:10.5px;text-transform:uppercase;letter-spacing:.05em}
.sw-n{white-space:nowrap;font-weight:600}.sw-u code{font-size:10.5px;word-break:break-all;background:#f6f6f6;padding:1px 4px;border-radius:3px}
.sw-c{border:1px solid #ddd;background:#fff;border-radius:6px;padding:3px 9px;font-size:11px;cursor:pointer;white-space:nowrap}
a{color:#0a58ca;text-decoration:none}
#gate{display:flex;align-items:center;justify-content:center;min-height:80vh}
#gate-card{border:1px solid #e5e5e5;border-radius:10px;padding:28px 30px;text-align:center}
#gate-card h2{margin:0 0 12px;font-size:15px}#gate-input{border:1px solid #ddd;border-radius:6px;padding:7px 10px;font-size:14px}
#gate-btn{border:none;background:#111;color:#fff;border-radius:6px;padding:8px 16px;font-size:13px;margin-left:6px;cursor:pointer}
#gate-err{color:#b42318;font-size:12px;margin-top:8px;min-height:14px}
body.locked #content{filter:blur(20px);pointer-events:none}
</style></head><body class="locked">
<div id="gate"><div id="gate-card"><h2>swap sheet</h2><form id="gate-form" onsubmit="return gateSubmit(event)"><input id="gate-input" type="password" placeholder="password" autocomplete="off" autofocus><button id="gate-btn" type="submit">Enter</button></form><div id="gate-err"></div></div></div>
<div id="content" hidden></div>
<script type="application/json" id="payload">__PAYLOAD__</script>
<script>
function b64ToBytes(b){const s=atob(b),a=new Uint8Array(s.length);for(let i=0;i<s.length;i++)a[i]=s.charCodeAt(i);return a}
async function deriveKey(p,salt,it){const e=new TextEncoder();const bk=await crypto.subtle.importKey("raw",e.encode(p),"PBKDF2",false,["deriveKey"]);return crypto.subtle.deriveKey({name:"PBKDF2",salt,iterations:it,hash:"SHA-256"},bk,{name:"AES-GCM",length:256},false,["decrypt"])}
async function decryptPayload(p){const b=JSON.parse(document.getElementById('payload').textContent);const key=await deriveKey(p,b64ToBytes(b.salt),b.iterations);const pl=await crypto.subtle.decrypt({name:"AES-GCM",iv:b64ToBytes(b.iv)},key,b64ToBytes(b.ciphertext));return new TextDecoder().decode(pl)}
function reveal(h){const c=document.getElementById('content');if(!c.hidden)return;c.innerHTML=h;c.hidden=false;document.getElementById('gate').style.display='none';document.body.classList.remove('locked')}
async function gateSubmit(e){e.preventDefault();const i=document.getElementById('gate-input'),err=document.getElementById('gate-err');err.textContent='';try{reveal(await decryptPayload(i.value));try{localStorage.setItem('card_swap_pw',i.value)}catch(_){}}catch(_){err.textContent='wrong password';i.value='';i.focus()}return false}
(async()=>{try{const c=localStorage.getItem('card_swap_pw');if(c)reveal(await decryptPayload(c))}catch(_){try{localStorage.removeItem('card_swap_pw')}catch(_){}}})();
</script></body></html>"""
open("index.html","w").write(html.replace("__PAYLOAD__", payload_json))
print("index.html written (gated)")
