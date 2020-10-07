$(document).ready(function () {
  /* Retrieve blog posts */
  var feedURL = "https://www.brainsorting.dev/rss.xml";
  var num_posts = 4;
  $.ajax({
    type: "GET",
    url: "https://api.rss2json.com/v1/api.json?rss_url=" + feedURL,
    dataType: "json",
    success: function (result) {
      display_posts(result.items.slice(0, num_posts));
    },
  });

  function display_posts(posts) {
    console.log(posts);
    var blog_posts = document.querySelector("#blog-posts");

    var container = new DocumentFragment();

    posts.forEach(function (post) {
      var child_container = new DocumentFragment();

      var child_div = document.createElement("div");
      child_div.className = "post";

      var child_content_div = document.createElement("div");
      child_content_div.className = "post-content";

      var child_div_link = document.createElement("a");
      child_div_link.href = post.link;
      child_div_link.target = "_blank";

      var title = document.createElement("h3");
      title.innerHTML = post.title;
      title.className = "title";

      child_div_link.appendChild(title);
      child_content_div.appendChild(child_div_link);
      child_div.appendChild(child_content_div);
      child_container.appendChild(child_div);
      container.appendChild(child_container);
    });
    blog_posts.appendChild(container);
  }
});
