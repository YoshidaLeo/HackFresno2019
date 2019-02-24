<html>
  <head>
  <link rel="stylesheet" href="../styles/index.css">
  </head>
  <body>
    <header>
      <h1>Teacher Tech Finder</h1>      
    </header>
    <br/>
    <img src="../images/TTF.png" width="100" height="100">
    <section>
    <?php 
    $servername = "localhost";
    $username = "user1";
    $password = "password";
    $dbname = "demodb";
    $where_clause = $_GET["variable"];
    

    $conn = new mysqli($servername, $username, $password, $dbname);
    
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 
    
    $sql = "SELECT name, url, rating, description, logo FROM HackFresno WHERE tags = $where_clause";
    $result = $conn->query($sql);
    
    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo "<div> <strong>". $row["name"]. "</strong><br/><img id=\"logo\" src=". $row["logo"]." width=75 height=75><br>Website: " . $row["url"] . "<br/>Rating:  ".$row["rating"]. "&#9734"."<br/>Description:  ".$row["description"] ."<div/> <br/><br/>";
        }
    } else {
        echo "0 results";
    }
    
    $conn->close();
    ?>
    </section>
  </body>
</html>