require('dotenv').config();
const username = process.env.tiktok_email
const password = process.env.tiktok_password
const LOGIN_URL = 'https://www.tiktok.com/login/phone-or-email/email';
const cookiesPath = './tiktok_cookies.json';

const puppeteer = require('puppeteer');
const fs = require('fs').promises;

(async () => {
  const browser = await puppeteer.launch({ 
    headless: false, 
    args: [
        "--disable-notifications"
  ] });
  const page = await browser.newPage();

// Uncomment this if you have cookies
  try {
    const cookies = JSON.parse(await fs.readFile(cookiesPath, 'utf8'));
    await page.setCookie(...cookies);
  } catch (error) {
    console.log('Cookies not found or cannot be loaded.');
  }

// Uncomment this if you are not login
//   await login(page, username, password);

  // Followers num
  await page.goto('https://www.tiktok.com/@aniesbaswedan');
  const followers_num = await page.evaluate(() => {
    const div = document.querySelector('strong[title="Followers"]');
    return div.textContent;
  });
  console.log('Value of the div:', followers_num);

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
  await page.type('input[type="password"]', password);
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
