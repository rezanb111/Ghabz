<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;700;900&display=swap');
body { font-family: 'Vazirmatn', sans-serif; background: #222; padding: 20px; }
.form { background: #fff; padding: 20px; border-radius: 10px; max-width: 500px; margin: 0 auto 20px; }
input { width: 90%; padding: 10px; margin: 5px 0; font-family: 'Vazirmatn'; }
button { width: 95%; padding: 10px; background: #007bff; color: #fff; border: none; cursor: pointer; font-weight: bold; }
#bill { background: #fff; width: 800px; margin: 0 auto; padding: 20px; border: 2px solid #000; display: none; }
.header { border-bottom: 2px solid #000; display: flex; justify-content: space-between; align-items: center; }
.footer { border-top: 1px solid #000; margin-top: 20px; display: flex; justify-content: space-between; padding-top: 10px; }
@media print { .form { display: none; } #bill { display: block !important; } }
</style>
</head>
<body>
<div class="form">
<input type="text" id="n" placeholder="نام" value="محسن سازنده اصفهانی">
<input type="text" id="p" placeholder="مبلغ (ریال)" value="۵۹۲,۰۰۰">
<input type="text" id="b" placeholder="شناسه قبض" value="۷۹۱۶۱۰۹۸۰۴۳۲۰">
<button onclick="run()">مشاهده و چاپ قبض</button>
</div>
<div id="bill">
<div class="header">
<img src="https://logoyab.com/wp-content/uploads/2025/03/Electricity-Department-Logo-1-1030x1030.png" width="60">
<h2>صورتحساب برق مصرفی</h2>
<div id="ob" style="font-size:12px"></div>
</div>
<p>نام مشترک: <b id="on"></b></p>
<h1 style="color:red; text-align:center">مبلغ قابل پرداخت: <span id="op"></span> ریال</h1>
<div class="footer">
<div><img src="https://uploadkon.ir/uploads/e17115_26IMG-۲۰۲۶۰۲۱۶-۰۳۱۵۲۱.jpg" width="80"><br>مأمور: علی ابریان</div>
<div style="text-align:left">سامانه برق ایران<br>Bargheman.com</div>
</div>
</div>
<script>
function run(){
document.getElementById('on').innerText = document.getElementById('n').value;
document.getElementById('op').innerText = document.getElementById('p').value;
document.getElementById('ob').innerText = 'شناسه: ' + document.getElementById('b').value;
document.getElementById('bill').style.display = 'block';
}
</script>
</body>
</html>
