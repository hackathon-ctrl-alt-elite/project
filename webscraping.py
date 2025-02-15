import requests
from bs4 import BeautifulSoup
import csv

def get_major_links(faculty_url):
    response = requests.get(faculty_url)
    if response.status_code != 200:
        print(f"Failed to retrieve faculty page: {faculty_url}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    major_links = []
    for link in soup.select("a[href^='/catalogue/course']"):
        major_links.append("https://apps.ualberta.ca" + link["href"])
    return major_links

def get_course_links(major_url):
    response = requests.get(major_url)
    if response.status_code != 200:
        print(f"Failed to retrieve major page: {major_url}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    course_links = []
    for link in soup.select("a[href^='/catalogue/course/']"):
        course_links.append("https://apps.ualberta.ca" + link["href"])
    return course_links

def scrape_course_page(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("h1").text.strip() if soup.find("h1") else "Unknown Title"
    description = soup.find("p").text.strip() if soup.find("p") else "No description available"
    
    return {
        "title": title,
        "description": description,
        "url": url
    }

def main():
    faculties = [
        "https://apps.ualberta.ca/catalogue/faculty/sc",  # Faculty of Science
        # Add more faculty URLs here
    ]
    
    courses = []
    for faculty_url in faculties:
        major_links = get_major_links(faculty_url)
        for major_url in major_links:
            course_links = get_course_links(major_url)
            for link in course_links:
                course_data = scrape_course_page(link)
                if course_data:
                    courses.append(course_data)
    
    with open("ualberta_courses.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["title", "description", "url"])
        writer.writeheader()
        writer.writerows(courses)
    
    print(f"Scraped {len(courses)} courses and saved to 'ualberta_courses.csv'")

if __name__ == "__main__":
    main()
