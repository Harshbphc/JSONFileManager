import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv('PASSWORD')
class json_files_model():
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host="dpg-ctrq2j3qf0us73dj0250-a.oregon-postgres.render.com",
                user="root",
                password="lY5ULvH4qbFdTeeypgLBsz3oa0wUX2Vy",
                database="json_files"
            )
            self.conn.autocommit = True
            self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
            print("Connection established")
        except Exception as e:
            print("Connection failed:", e)

    def jsonfile_create(self, filename, category):
        print(filename, category)
        try:
            query = """
            INSERT INTO public.json_file_names (json_file_name, category)
            VALUES (%s, %s)
            """
            self.cur.execute(query, (filename.lower(), category.lower()))
            print("Executed successfully")
        except Exception as e:
            print("Failed to execute:", e)

    def fetch_categories(self):
        try:
            query = "SELECT DISTINCT category FROM public.json_file_names"
            self.cur.execute(query)
            categories = [row["category"] for row in self.cur.fetchall()]
            print("Categories fetched successfully")
            return categories
        except Exception as e:
            print("Failed to fetch categories:", e)
            return []

    def fetch_files_for_category(self, category):
        try:
            query = """
            SELECT json_file_name 
            FROM public.json_file_names 
            WHERE category = %s
            """
            self.cur.execute(query, (category,))
            files = [row["json_file_name"] for row in self.cur.fetchall()]
            print(f"Files fetched successfully for category: {category}")
            return files
        except Exception as e:
            print("Failed to fetch files for the category:", e)
            return []