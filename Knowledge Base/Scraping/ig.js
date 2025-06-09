require('dotenv').config();
const username = process.env.username
const password = process.env.password


const puppeteer = require('puppeteer');
const fs = require('fs').promises;


const LOGIN_URL = 'https://www.instagram.com/accounts/login/';

(async () => {
  const browser = await puppeteer.launch({ 
    headless: false, 
    args: [
        "--disable-notifications"
  ] });
  const page = await browser.newPage();

  // Load cookies if available
  const cookiesPath = './ig_cookies.json';
  try {
    const cookies = JSON.parse(await fs.readFile(cookiesPath, 'utf8'));
    await page.setCookie(...cookies);
  } catch (error) {
    console.log('Cookies not found or cannot be loaded.');
  }

//   // Navigate to Instagram and check login status
//   await page.goto('https://www.instagram.com/');
//   const isLoggedIn = await page.$('a[href="/accounts/login/"]') === null;

//   if (!isLoggedIn) {
//     console.log('Already logged in.');
//   } else {
//     console.log('Not logged in. Logging in...');
//     await login(page, username, password);
//   }

  /* Per post */ 

  // await page.goto('https://www.instagram.com');
  // // Scroll to load more posts
  // await autoScroll(page, 2);

  // // Extract post links
  // const postLinks = await page.evaluate(() => {
  //   const posts = document.querySelectorAll('a[href^="/p/"]');
  //   return Array.from(posts).map(post => post.getAttribute('href'));
  // });

  // console.log(postLinks)

  // Like each post
//   for (const postLink of postLinks) {
//     await page.goto(`https://www.instagram.com${postLink}`);
//     await page.waitForSelector('button svg[aria-label="Like"]');
//     await page.click('button svg[aria-label="Like"]');
//     console.log(`Liked post: https://www.instagram.com${postLink}`);
//     await page.waitForTimeout(3000); // Wait for a moment to avoid detection
//   }

  /* Followers */ 
  await page.goto(`https://www.instagram.com/${username}/followers/`);
  await page.waitForNavigation({ waitUntil: 'domcontentloaded' });

  await autoScroll(page);

  // Extract list of all username links
  // const usernames = await page.evaluate(() => {
  //   const usernameElements = document.querySelectorAll('span._ap3a');
  //   return Array.from(usernameElements).map(span => span.textContent.trim());
  // });

//   // Log the usernames
//   console.log('Usernames:', usernames);

  // Close the browser
  await browser.close();

})();

async function login(page, username, password) {
  // Navigate to the login page
  await page.goto(LOGIN_URL);

  // Wait for the login page to load
  await page.waitForSelector('input[name="username"]');

  // Fill in the login form and submit
  await page.type('input[name="username"]', username);
  await page.type('input[name="password"]', password);
  await page.click('button[type="submit"]');

  // Save cookies for future sessions
  const currentCookies = await page.cookies();
  await fs.writeFile(cookiesPath, JSON.stringify(currentCookies, null, 2));

  // Wait for navigation after login
//   await page.waitForNavigation();
}

async function autoScroll(page, numberOfPosts) {
    let postsLoaded = 0;
  
    await page.evaluate(async (numberOfPosts) => {
      await new Promise((resolve) => {
        let totalHeight = 0;
        const distance = 100;
        const scrollInterval = setInterval(() => {
          const scrollHeight = document.body.scrollHeight;
          window.scrollBy(0, distance);
          totalHeight += distance;
  
          if (totalHeight >= scrollHeight || postsLoaded >= numberOfPosts) {
            clearInterval(scrollInterval);
            resolve();
          }
        }, 100);
      });
    }, numberOfPosts);
  }
