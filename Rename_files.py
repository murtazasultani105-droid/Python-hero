import os

def rename_files(folder_path, prefix, start_number=1, extension=None):
    # گرفتن لیست فایل‌ها
    files = os.listdir(folder_path)

    # مرتب‌سازی فایل‌ها
    files.sort()

    number = start_number
    for file_name in files:
        # ساخت مسیر کامل فایل
        old_path = os.path.join(folder_path, file_name)

        # اگر این یک پوشه باشد، رد شود
        if os.path.isdir(old_path):
            continue

        # پسوند فایل
        file_ext = os.path.splitext(file_name)[1]

        # اگر کاربر پسوند مشخص کرده باشد
        if extension:
            file_ext = extension

        # نام جدید
        new_name = f"{prefix}_{number:03d}{file_ext}"
        new_path = os.path.join(folder_path, new_name)

        # تغییر نام فایل
        os.rename(old_path, new_path)
        number += 1

    print("Rename completed!")

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    prefix = input("Enter new prefix: ")
    start = int(input("Start number (example 1): "))
    ext = input("Extension (leave blank to keep original): ")

    if ext == "":
        ext = None

    rename_files(folder, prefix, start, ext)