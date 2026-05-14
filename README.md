<!DOCTYPE html>
<html lang="ar">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Social Downloader</title>

<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    background:#0f0f0f;
    font-family:Arial, sans-serif;
    color:white;
    padding:20px;
}

.header{
    text-align:center;
    margin-top:30px;
    margin-bottom:40px;
}

.header h1{
    font-size:32px;
    margin-bottom:10px;
}

.header p{
    color:#999;
    font-size:16px;
}

.container{
    width:100%;
    max-width:350px;
    margin:auto;
}

.card{
    width:100%;
    min-height:75px;
    border-radius:18px;
    margin-bottom:20px;
    display:flex;
    align-items:center;
    gap:15px;
    padding:20px;
    text-decoration:none;
    color:white;
    font-size:24px;
    font-weight:bold;
    transition:0.3s;
}

.card:hover{
    transform:scale(1.03);
}

.youtube{
    background:red;
}

.facebook{
    background:#1877F2;
}

.instagram{
    background:linear-gradient(
    45deg,
    #feda75,
    #fa7e1e,
    #d62976,
    #962fbf,
    #4f5bd5
    );
}

.tiktok{
    background:black;
    border:2px solid white;
}

i{
    font-size:34px;
}

.footer{
    text-align:center;
    margin-top:40px;
    color:#666;
    font-size:18px;
}

</style>

</head>

<body>

<div class="header">

<h1>Social Downloader</h1>

<p>
تحميل الفيديوهات من السوشيال ميديا
</p>

</div>

<div class="container">

<a href="youtube.html" class="card youtube">
<i class="fab fa-youtube"></i>
YouTube
</a>

<a href="facebook.html" class="card facebook">
<i class="fab fa-facebook"></i>
Facebook
</a>

<a href="instagram.html" class="card instagram">
<i class="fab fa-instagram"></i>
Instagram
</a>

<a href="tiktok.html" class="card tiktok">
<i class="fab fa-tiktok"></i>
TikTok
</a>

</div>

<div class="footer">
Made By Tish 🔥
</div>

</body>
</html>