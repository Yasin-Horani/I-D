import instaloader

L = instaloader.Instaloader(save_metadata=False, download_video_thumbnails=False)

# Optional: Login to access private posts or higher resolution
username = "username"
password = "******"
# This will save a session to speed up next login
L.login(username, password)

# Download a single post (e.g., video)
post_url = "https://www.instagram.com/reel/xxxxxxxxxxxxxxxx/"
post_shortcode = post_url.rstrip('/').split('/')[-1]
post = instaloader.Post.from_shortcode(L.context, post_shortcode)

# Check if it contains a video
if post.is_video:
    print("Downloading video...")
    L.download_post(post, target=f"{post.owner_username}_video")
else:
    print("This post does not contain a video.")
