<?php 
$name = $_POST['name'];
$email = $_POST['email'];
$content =  $_POST['content'];

if (empty($name) || empty($email) || empty($content) || !preg_match("/([\w\-]+\@[\w\-]+\.[\w\-]+)/",$email)) {
    header('HTTP/1.0 406 NOT_ACCEPTABLE');
    return ;
};

$to = "qiujing@kean.edu"; // should be in configure file, whatever
$subject = "Contact info from TECH STATION, " . $name;
$txt = $content . "<br/>From : " . $email . "<br/>Name : " . $name;
$headers = "From: $email";

mail($to, $subject, $txt, $headers);
header('HTTP/1.0 200');
?>