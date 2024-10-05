import os
import shutil
import sys


def copy_files(src, dest):
    try:
        if not os.path.exists(src):
            print(f"Error: Source directory '{src}' does not exist.")
            return

        if not os.path.exists(dest):
            os.makedirs(dest)

        for item in os.listdir(src):
            item_path = os.path.join(src, item)

            if os.path.isdir(item_path):
                copy_files(item_path, dest)
            elif os.path.isfile(item_path):
                file_extension = os.path.splitext(item)[1][1:]
                if not file_extension:
                    file_extension = "unknown"

                target_dir = os.path.join(dest, file_extension)

                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                try:
                    shutil.copy2(item_path, target_dir)
                    print(f"Copied file '{item_path}' to '{target_dir}'")
                except Exception as e:
                    print(f"Failed to copy file '{item_path}': {e}")

    except Exception as e:
        print(f"Error during file copying: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python script_name.py <source_directory_path> [<destination_directory_path>]"
        )
        sys.exit(1)

    src = sys.argv[1]
    dest = sys.argv[2] if len(sys.argv) > 2 else "dist"

    copy_files(src, dest)
