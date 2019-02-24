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
    $temp = (string)$where_clause;
    
    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 
    
    $sql = "SELECT name, url, tags, rating FROM HackFresno WHERE (tags = $where_clause) OR (name = $where_clause) OR (url = $where_clause) OR (rating = $where_clause)";
    $result = $conn->query($sql);
    
    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo "<div> Name: ". $row["name"]. "Website: " . $row["url"] . " - Rating: ".$row["rating"]. "<div/> <br/>";
        }
    } else {
        echo "No result Found";
    }
    
    $conn->close();
    ?>
    </section>
  </body>
</html>