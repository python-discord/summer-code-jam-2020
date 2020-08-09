<?php
    $data_file = fopen("user_code.txt","w");
    $user_code = $_POST["code"];
    fwrite($data_file);
    fclose($data_file);

?>