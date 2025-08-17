# File Handling and Exception Handling Assignment
# This program demonstrates file operations and error handling as taught in class

import os

def file_read_write_challenge():
    """
    Challenge 1: File Read & Write Challenge 🖋️
    Reads a file and writes a modified version to a new file
    """
    print("=" * 50)
    print("FILE READ & WRITE CHALLENGE")
    print("=" * 50)
    
    sample_content = """Welcome to Python File Handling!
This is line 2 of our sample file.
Python makes file operations easy.
Learning file handling is important.
Exception handling keeps our code safe."""
    
    try:
        with open("input_sample.txt", "w") as file:
            file.write(sample_content)
        print("✅ Sample input file 'input_sample.txt' created successfully!")
        
        with open("input_sample.txt", "r") as input_file:
            original_content = input_file.read()
            print("\n📖 Original file content:")
            print("-" * 30)
            print(original_content)
        
        lines = original_content.split('\n')
        modified_lines = []
        for i, line in enumerate(lines, 1):
            if line.strip():  
                modified_line = f"{i}. {line.upper()}"
                modified_lines.append(modified_line)
        
        modified_content = '\n'.join(modified_lines)
        
        with open("modified_output.txt", "w") as output_file:
            output_file.write("MODIFIED VERSION OF THE FILE\n")
            output_file.write("=" * 40 + "\n")
            output_file.write(modified_content)
            output_file.write("\n\n--- End of Modified File ---")
        
        print("\n📝 Modified file content:")
        print("-" * 30)
        print("MODIFIED VERSION OF THE FILE")
        print("=" * 40)
        print(modified_content)
        print("\n--- End of Modified File ---")
        
        print("\n✅ Modified content written to 'modified_output.txt' successfully!")
        
    except FileNotFoundError as e:
        print(f"❌ Error: File not found - {e}")
    except PermissionError as e:
        print(f"❌ Error: Permission denied - {e}")
    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")
    finally:
        print("\n🔒 File operations completed.")

def error_handling_lab():
    """
    Challenge 2: Error Handling Lab 🧪
    Ask user for filename and handle errors if it doesn't exist or can't be read
    """
    print("\n" + "=" * 50)
    print("ERROR HANDLING LAB")
    print("=" * 50)
    
    max_attempts = 3
    attempt = 0
    
    while attempt < max_attempts:
        try:
            filename = input(f"\n📁 Enter a filename to read (Attempt {attempt + 1}/{max_attempts}): ").strip()
            
            if not filename:
                raise ValueError("Filename cannot be empty!")
            
            if not os.path.exists(filename):
                raise FileNotFoundError(f"The file '{filename}' does not exist.")
            
            with open(filename, "r") as file:
                content = file.read()
                
                if not content.strip():
                    print("⚠️  Warning: The file is empty!")
                else:
                    print(f"\n✅ Successfully read '{filename}'!")
                    print("-" * 40)
                    print("File content:")
                    print(content)
                    print("-" * 40)
                    print(f"📊 File statistics:")
                    print(f"   • Characters: {len(content)}")
                    print(f"   • Lines: {len(content.splitlines())}")
                    print(f"   • Words: {len(content.split())}")
                
                break 
                
        except FileNotFoundError as e:
            print(f"❌ File Error: {e}")
            attempt += 1
            if attempt < max_attempts:
                print("💡 Tip: Make sure the file exists in the current directory.")
                create_sample = input("Would you like me to create a sample file? (y/n): ").lower()
                if create_sample == 'y':
                    create_sample_file()
        
        except PermissionError as e:
            print(f"❌ Permission Error: Cannot read '{filename}' - {e}")
            attempt += 1
            if attempt < max_attempts:
                print("💡 Tip: Check if you have permission to read this file.")
        
        except ValueError as e:
            print(f"❌ Input Error: {e}")
            attempt += 1
        
        except UnicodeDecodeError as e:
            print(f"❌ Encoding Error: Cannot decode '{filename}' - {e}")
            print("💡 Tip: This might be a binary file. Try a text file instead.")
            attempt += 1
        
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")
            attempt += 1
        
        finally:
            if attempt < max_attempts:
                print(f"🔄 {max_attempts - attempt} attempts remaining...")
    
    if attempt >= max_attempts:
        print("\n⚠️  Maximum attempts reached. Lab session ended.")
        print("💡 Remember: Always check file paths and permissions!")

def create_sample_file():
    """Helper function to create a sample file for testing"""
    try:
        sample_files = {
            "test_file.txt": "Hello World!\nThis is a test file.\nPython file handling is awesome!",
            "numbers.txt": "1\n2\n3\n4\n5\n6\n7\n8\n9\n10",
            "empty_file.txt": ""
        }
        
        print("\n🛠️  Creating sample files...")
        for filename, content in sample_files.items():
            with open(filename, "w") as file:
                file.write(content)
            print(f"   ✅ Created: {filename}")
        
        print("✨ Sample files created successfully!")
        
    except Exception as e:
        print(f"❌ Error creating sample files: {e}")

def demonstrate_file_modes():
    """Bonus: Demonstrate different file modes as taught in class"""
    print("\n" + "=" * 50)
    print("BONUS: FILE MODES DEMONSTRATION")
    print("=" * 50)
    
    try:
        print("\n📝 Demonstrating Write mode ('w'):")
        with open("demo_write.txt", "w") as file:
            file.write("This file was created in write mode.\n")
            file.write("Write mode overwrites existing content.\n")
        print("✅ Content written to 'demo_write.txt'")
        
        print("\n📝 Demonstrating Append mode ('a'):")
        with open("demo_write.txt", "a") as file:
            file.write("This line was added in append mode.\n")
            file.write("Append mode preserves existing content.\n")
        print("✅ Content appended to 'demo_write.txt'")
        
        print("\n📖 Reading final content:")
        with open("demo_write.txt", "r") as file:
            content = file.read()
            print("-" * 30)
            print(content)
            print("-" * 30)
        
        print("\n📖 Demonstrating readline() and readlines():")
        with open("demo_write.txt", "r") as file:
            print("Using readline():")
            first_line = file.readline()
            print(f"   First line: {first_line.strip()}")
        
        with open("demo_write.txt", "r") as file:
            print("Using readlines():")
            all_lines = file.readlines()
            for i, line in enumerate(all_lines, 1):
                print(f"   Line {i}: {line.strip()}")
        
    except Exception as e:
        print(f"❌ Error in demonstration: {e}")
    finally:
        print("\n🔒 File modes demonstration completed.")

def main():
    """Main function to run all challenges"""
    print("🐍 PYTHON FILE HANDLING & EXCEPTION HANDLING ASSIGNMENT")
    print("Based on Beginner Class Teachings")
    print("=" * 60)
    
    try:
        file_read_write_challenge()
        
        error_handling_lab()
        
        demonstrate_file_modes()
        
        print("\n" + "=" * 60)
        print("🎉 ASSIGNMENT COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print("📚 Key Concepts Demonstrated:")
        print("   ✅ File opening in different modes ('r', 'w', 'a')")
        print("   ✅ Reading files (.read(), .readline(), .readlines())")
        print("   ✅ Writing and appending to files")
        print("   ✅ Using 'with' statement for automatic file closing")
        print("   ✅ Exception handling (try-except-finally)")
        print("   ✅ Specific error types (FileNotFoundError, PermissionError)")
        print("   ✅ Best practices for robust file handling")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user.")
    except Exception as e:
        print(f"\n❌ Fatal error in main program: {e}")
    finally:
        print("\n👋 Thank you for running the assignment!")
        print("💡 Remember: Always handle exceptions and close files properly!")

if __name__ == "__main__":
    main()