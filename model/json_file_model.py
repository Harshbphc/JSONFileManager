import mysql.connector

class json_files_model():
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", passwd="harsh", database="json_files")
            self.conn.autocommit = True
            self.cur = self.conn.cursor(dictionary=True)
            print("Connection established")
        except:
            print("Connection failed")
    def jsonfile_create(self, filename, category):
        print(filename, category)
        try:
            self.cur.execute(f"INSERT INTO json_file_names(json_file_name, category) VALUES('{filename.lower()}', '{category.lower()}')")
            print("executed successfully")
        except:
            print("failed")

    def fetch_categories(self):
        try:

            self.cur.execute("SELECT DISTINCT category FROM json_file_names")

            categories = [row["category"] for row in self.cur.fetchall()]
            print("Categories fetched successfully")

            return categories
        except Exception as e:
            print("Failed to fetch categories:", e)
            return []
        
    def fetch_files_for_category(self, category):
        try:

            self.cur.execute("SELECT json_file_name FROM json_file_names WHERE category = %s", (category,))
        
            # Fetch all results and extract file names
            files = [row["json_file_name"] for row in self.cur.fetchall()]
            print(f"Files fetched successfully for category: {category}")
            return files
        except Exception as e:
            print("Failed to fetch files for the category", e)
            return []