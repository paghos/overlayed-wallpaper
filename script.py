from PIL import Image
import os

def overlay_images(base_image_path, overlay_image_path, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)
        base_images = os.listdir(base_image_path)
        
        for image_file in base_images:
            base_image = Image.open(os.path.join(base_image_path, image_file))
            overlay_image = Image.open(overlay_image_path)
            
            # Resize overlay image to match the base image's dimensions with antialiasing
            overlay_image = overlay_image.resize(base_image.size, Image.LANCZOS)
            
            # Create a transparent overlay
            overlay = Image.new("RGBA", base_image.size, (0, 0, 0, 0))
            overlay.paste(overlay_image, (0, 0), overlay_image)
            
            # Combine base image and overlay
            combined_image = Image.alpha_composite(base_image.convert("RGBA"), overlay)
            
            # Save the output image
            output_path = os.path.join(output_dir, f"Overlay_{image_file}")
            combined_image.save(output_path, format="PNG")
            
        print("Image overlays completed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    base_image_directory = r"C:\Users\AnotherOneBitesTheDust\Desktop\Wallpaper\Img"
    overlay_image_path = r"C:\Users\AnotherOneBitesTheDust\Desktop\Wallpaper\OverlayWallpaper.png"
    output_directory = r"C:\Users\AnotherOneBitesTheDust\Desktop\Wallpaper\ImgOut"
    
    overlay_images(base_image_directory, overlay_image_path, output_directory)
