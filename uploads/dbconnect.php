<?php


 // echo "<br>" .var_dump($_REQUEST) ;  
 
 $user_id =           $_REQUEST['user_id']          ?? "null"; //получаем "id"
 $user_description =  $_REQUEST['user_description'] ?? "null";  
 $address=            $_REQUEST['address']          ?? "null";  
 $status=             $_REQUEST['status']           ?? "null"; 
 $volt=               $_REQUEST['volt']             ?? "null" ;  
 $description =       $_REQUEST['description']      ?? "null";  


 echo "<br> " . $user_id."<br> " . $user_description."<br> " . "$address"."<br> " . "$status"."<br> " . $volt."<br> " . $description ;


$servername = "mikola1601.zzz.com.ua:3306";
$database = "mikola1601";
$username = "MIKOLA1601";
$password = "Hm134549";
$connect = mysqli_connect($servername, $username, $password, $database);
if (!$connect) {
    die("<br> Ошибка подключения: " . mysqli_connect_error());
}
echo "<br> Подключение к БД прошло успешно.";

# Сервер: ", $servername, ", БД: ", $database, ", пользователь: ", $username;




# $query = mysqli_query($connect, "INSERT INTO  bot (`user_id`, `address`, `user_description`, `status`, `description`, `volt`) VALUES($user_id, $address, $user_description, $status, $description, $volt ) ");
$query = mysqli_query($connect, "INSERT INTO  bot (`user_id`, `address`, `user_description`, `status`, `description`, `volt`)
                                            VALUES('$user_id', '$address', '$user_description', '$status', '$description', '$volt' ) ");
                                            
if (mysqli_query($connect, $sql)) {
      echo "New record  successfully";
} else {
      echo "<br>" . "Error  SQL: " . $sql . mysqli_error($connect);
}





#$query= mysqli_query($connect, " SELECT * FROM bot ");
#                   
#if (mysqli_query($connect, $sql)) {
#      echo "Find ok" . $sql .  mysqli_error($connect); 
#} else {
#      echo "<br>" . "Error in SQL: " .  mysqli_query($connect, 0);
#}



$sql = "SELECT * FROM bot  where user_id ='4831b7932bbc'   order by time DESC limit 1  " ;
$queryRes = mysqli_query($connect, $sql);
$result = mysqli_fetch_array($queryRes);
echo "<br>" .  $result[1];



# SELECT * from bot   where (user_id ='4831b7932bbc') order by time DESC limit 1; 




echo('<html>
<head>
<meta charset="utf-8">
<title>MySQL or MariaDB query example</title>
</head>
<body>');





?>
















