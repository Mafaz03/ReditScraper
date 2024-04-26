def show_images(links, title = None, figsize=(15,15), sub_title=None, noframe=True, max_col = 6, max_size=500, max_images = None, fontsize = 10, **kwargs):
  transform = transforms.ToTensor()
  if isinstance(links, str): links = [links]
  if max_images: num_images = min(len(links), max_images)
  else: num_images = len(links)
  num_rows = (num_images - 1) // max_col + 1
  fig, axes = plt.subplots(num_rows, max_col, figsize=figsize)
  if num_images > 1: axes = axes.flatten()
  if sub_title:
    if isinstance(sub_title, list) and len(sub_title) == num_images: pass
    elif isinstance(sub_title, str): sub_title = [sub_title] * num_images
    else: sub_title = [''] * num_images
  for i, link in enumerate(links[:num_images]):
    try: response = requests.get(link)
    except: pass
    finally:
      try:
        image = Image.open(BytesIO(response.content))
        image.thumbnail((max_size, max_size), Image.LANCZOS)
        if image.mode != 'RGB': image = image.convert('RGB')
        img_tensor = transform(image)
        if img_tensor.shape[0] == 3: img_tensor = img_tensor.permute(1, 2, 0)
        np_image = np.array(img_tensor)
        if sub_title:
          word = sub_title[i] if len(sub_title[i]) <= 45 else ""
          axes[i].set_title(word, fontsize = fontsize)
        axes[i].imshow(np_image, **kwargs)
      except: pass
    if noframe: axes[i].axis('off')
  for j in range(i + 1, num_rows * max_col):
      axes[j].axis('off')
  if title: plt.suptitle(title)
  plt.tight_layout()
  plt.show()
