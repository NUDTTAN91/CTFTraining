<?php
require 'class/header.php';
session_destroy();
// header("location: ./index.php");
echo "<script>window.location.href='./index.php'</script>";
exit;
?>