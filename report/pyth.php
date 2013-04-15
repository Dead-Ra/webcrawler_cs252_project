<?php
	$flag=0;
	$database=0;
	if(isset($_POST["conf"])){
		if(($_POST["conf"]!= NULL)){
			$con = mysql_connect("localhost","root","123");
			if (!$con)
			{
			  die('Could not connect: ' . mysql_error());
			}

			mysql_select_db("crawler", $con);
			$fav_link = array();
			$flag=1;
			$data=$_POST["type"];
			$confer=$_POST["conf"];
			$i=$confer[0];
			$j=ord(strtolower($i)) - 96;
			$table="table".$j;
			$re="SELECT * FROM $table WHERE Acronym ='$confer'";
			$result=mysql_query($re,$con);
			$count= mysql_num_rows($result);
			/*if($count==1)
			{
				$database=1;
				echo "the details:<br>";
				while($row = mysql_fetch_assoc($result))
				{
					echo "sr no:".$row['Sr_no']."<br>Acronym  -".$row['Acronym']."<br>Dates  ".$row['Dates']."<br>Links ".$row['Links']."<br><br>";
					$link = $row['Links'];
				}
			}
			else{*/
				$x = "crawl.py ";
				$shell = 'python '.$x.'"'.$confer.' conference 2013 '.$data.'"';
				$output = shell_exec($shell);
				$lines = explode(PHP_EOL, $output);
				//echo "<pre>";
				//print_r ($lines);
				//echo "</pre>";
				$flagfav=0;
				$fav_link[] = $lines[1];
				$date = $lines[2];
				for($r=4;$r<count($lines)-1;$r++)
				{
						$fav_link[]=$lines[$r];
				}
				$link = $fav_link[0];
				$query="INSERT INTO $table (Acronym, Type, Dates, Links) VALUES ('$confer','$data','$date','$fav_link[0]')";
				mysql_query($query,$con);
				mysql_close($con);
			//}
		}
	}
	else{
		$flag=0;
	}
?>
<html>
	<head>
		<title>The Conference Manager</title>
	</head>
	<body>
		<div>
			<br>
			<form method="POST" action="pyth.php">
				Conference Acronym: <input type="text" id="conf" name="conf">
				Conference Type: <input type="text" id="type" name="type">
				<button type="submit">Search</button>
			</form>
		</div>

		<div style="border:1px dotted black;padding:2em;width:70%;margin-left:auto;margin-right:auto">
			<p>
				<?php
					if($flag==1){
						echo "<h1 style='font-size:2.0em;'>Important Dates And Deadlines:</h1><br>";
						echo "<h2>".$confer."</h2><br>";
						echo "<h2>Deadline: ".$date."</h2><br>";
					}
					else{
						echo "Please enter the Conference Name and the type of conference tofind out the deadline.";
					}
				?>
			</p>
		</div>

		<div>
		<h3><b>Important Links related to the Conference:-</b></h3>
		<?php
			if($database==0){
				for ($i=0;$i<count($fav_link);$i++) {
					echo "<a href='" . $fav_link[$i] . "' target='_blank'>". $fav_link[$i] . "</a><br>";
				}
			}
			else{
				echo "-->".$link;
			}
		?>
		</div>
	</body>
</html>
