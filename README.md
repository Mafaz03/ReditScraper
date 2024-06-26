<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <h1>Scrapedit</h1>

  <h2>Overview</h2>

  <p>Scrapedit is a Python class designed for scraping images from Reddit subreddits and creating PyTorch datasets. It facilitates the collection of image data from various subreddits, allowing for easy integration into machine learning pipelines or data analysis projects.</p>

  <h2>Key Features</h2>

  <ul>
    <li><strong>Reddit Scraping:</strong> Automatically retrieves image URLs from specified subreddits using the PRAW library.</li>
    <li><strong>Flexible Configuration:</strong> Users can customize parameters such as subreddit names, post limits, sorting methods, and content safety filters.</li>
    <li><strong>Data Transformation:</strong> Supports image transformation and resizing to fit specific requirements.</li>
    <li><strong>Error Handling:</strong> Handles invalid subreddits, restricted subreddits, and failed image fetching gracefully, ensuring smooth data collection.</li>
    <li><strong>Data Visualization:</strong> Provides visualization tools to understand the distribution of data sources across different subreddits.</li>
  </ul>

  <h2>Usage</h2>

  <ol>
    <li><strong>Initialization:</strong> Instantiate the ScrapeditDataset class with a list of subreddit names and optional parameters for customization.</li>
    <li><strong>Data Loading:</strong> Access the dataset like any other PyTorch dataset, allowing for seamless integration into machine learning workflows.</li>
    <li><strong>Data Analysis:</strong> Use the provided visualization functions to gain insights into the distribution of data sources and explore the collected dataset.</li>
    <li><strong>Model Training:</strong> Utilize the ScrapeditDataset as a DataLoader for training machine learning models. Integrate it with PyTorch's DataLoader for efficient batch processing and model training.</li>
  </ol>

  <h2>Requirements</h2>

  <ul>
    <li>Python 3.x</li>
    <li>PRAW</li>
    <li>pandas</li>
    <li>requests</li>
    <li>matplotlib</li>
    <li>Pillow</li>
    <li>torch</li>
    <li>torchvision</li>
    <li>tqdm</li>
  </ul>

  <h2>Acknowledgements</h2>

  <ul>
    <li><a href="https://praw.readthedocs.io/en/latest/">PRAW</a>: The Python Reddit API Wrapper</li>
    <li><a href="https://github.com/tqdm/tqdm">tqdm</a>: A Fast, Extensible Progress Bar for Python and CLI</li>
    <li><a href="https://python-pillow.org/">Pillow</a>: The Python Imaging Library</li>
  </ul>

  <h2>License</h2>

  <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p>
</body>
</html>
