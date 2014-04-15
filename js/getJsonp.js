var json_data = [];
      function showOut(data, page)
      {
        //if (page == 1)
        //{
          //alert("page1");
        for (var i = ((page-1) * 10); i < (page*10); i++)
        {
          //alert(json_data[i].link);
          document.getElementById(i+1-(page-1)*10).href = data[i].link;
          document.getElementById(i+1-(page-1)*10).innerHTML = data[i].title;
          document.getElementById(i+11-(page-1)*10).innerHTML = data[i].snippet;
          document.getElementById(i+21-(page-1)*10).innerHTML = "(" + data[i].hits + " hits)";
        }
        //}
        $('#content').show();
      }

      function getSnippet(result)
      {
        //alert("getSnippet");
        var totalhits = result.query.searchinfo.totalhits;
        var snippet_title = result.query.search[0].title;
        //alert(snippet_title);
        var snippet = result.query.search[0].snippet;
        //alert(snippet);
        //alert(result.query.search[0].title + "  " + result.query.searchinfo.totalhits + "  " + result.query.search[0].snippet);
        for (key in json_data)
        {
          if (json_data[key].title == snippet_title)
          {
            //alert(json_data[key].title);
            json_data[key].snippet = snippet;
            json_data[key].hits = totalhits;
            //console.log(json_data[key].title + "             " + json_data[key].snippet);
            //alert(json_data[key].snippet + "  " + json_data[key].hits);
          }
        }
        showOut(json_data, 1);
      }

      function querySnippet(json)
      {
          //alert("here");
          for (x in json)
          {
            if (json[x].title == "Deaths in 2009" || json[x].title == "Deaths in 2013" || json[x].title == "Deaths in 2010")
            {
              json_data[x].snippet = "This is a list of lists of <span class='searchmatch'>deaths</span>, organized by year.  <span class='searchmatch'>Deaths</span> <span class='searchmatch'>in</span> CURRENTMONTHNAME CURRENTYEAR ), and then linked here.";
              json_data[x].hits = 421168;
            }
            //alert(json[x].title + json[x].link);
            var JSONP2 = document.createElement("script");  
            JSONP2.type = "text/javascript";  
            JSONP2.src = "http://en.wikipedia.org/w/api.php?format=json&action=query&list=search&srwhat=text&srsearch=";
            JSONP2.src = JSONP2.src + json[x].title + "&srlimit=1&callback=getSnippet"; 
            
            //alert(JSONP2.src);
            document.getElementsByTagName("head")[0].appendChild(JSONP2);  
          }
      }

      function getTitle(result) {  
        //alert(result.query.querypage.name); 
        var time_stamp = result.query.querypage.cachedtimestamp; 
        document.getElementById("time_stamp").innerHTML = time_stamp;
        
        
        //alert("time_stamp: " + time_stamp);
        var title_array = eval(result.query.querypage.results);
        for (x in title_array)
        {
          var links = "https://en.wikipedia.org/wiki/";
          //alert(title_array[x].title);
          //json_data[x] = title_array[x].title;
          links = links + title_array[x].title;
          //alert(links);
          json_data.push({"title": title_array[x].title, "link" : links, "snippet" : "", "hits" : 0});
          //document.getElementById("content").innerHTML=title_array[x].title;
          //alert(json_data[x].title + json_data[x].link);
        }
        querySnippet(json_data);
      }  

    function nextPage()
    {
      //alert("page2");
      showOut(json_data, 2);
      //document.getElementById("previous").className = "";
      //document.getElementById("next").className = "disabled";
    }

    function previousPage()
    {
      //alert("page1");
      showOut(json_data, 1);
    }
      