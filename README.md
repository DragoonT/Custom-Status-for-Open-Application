# Custom Playing Status for Open Application

Easily customize your Discord playing status with an image.

## Download

1. [Download Python](https://www.python.org/downloads/) or [Install Python from the Microsoft Store](https://www.microsoft.com/store/productId/9NRWMJP3717K?ocid=pdpshare)
2. [Add Python to PATH](https://www.mygreatlearning.com/blog/add-python-to-path/)
3. [Download Visual Studio Code](https://code.visualstudio.com/download) or [Download PyCharm](https://www.jetbrains.com/products/compare/?product=pycharm-ce&product=pycharm)
4. [CustomStatusDiscord.exe](https://github.com/DragoonT/Custom-Status-for-Open-Application/releases) (full version)
5. BiliBili Custom Status Discord! [BiliBiliCustomStatusDiscord.exe](https://github.com/DragoonT/BiliBili-Custom-Status/releases)
6. iQIYI Custom Status Discord! [iQIYICustomStatusDiscord.exe](https://github.com/DragoonT/iQIYI-Custom-Status/releases)
7. YouTube Custom Status Discord! [YouTubeCustomStatusDiscord.exe](https://github.com/DragoonT/YouTube_CustomStatus/releases)

## How to Create This Project (from howtoactivate.txt)

1. **Create a virtual environment:**
```bash
   python -m venv myenv
```
2. **Activate the virtual environment:**
   - On Windows (Command Prompt):
     `myenv\\Scripts\\activate`
   - On Windows (PowerShell):
     `.\\venv\\Scripts\\Activate`
   - On Linux/MacOS:
     `source venv/bin/activate`

3. **Install the required dependencies:**
```bash
   pip install -r requirementsOld.txt  # or requirements.txt
```
4. **Run the project:**
```bash
   python test.py  # You can rename test.py
```
If the environment doesn't work due to an incorrect Python version:

1. **Check the Python version:**
```bash
   where python # pythonX.XX
```
2. **Ensure the correct Python version is added to your system's PATH environment variables.**

Alternatively, you can specify the desired Python version:

1. **Create the virtual environment with a specific Python version:**
```bash
   pythonX.XX -m venv myenv  # Replace X.XX with the version (e.g., 3.7.9, 3.11.9, etc.)
```
2. **Activate the virtual environment:**
   - On Windows (Command Prompt):
     `myenv\\Scripts\\activate`
   - On Windows (PowerShell):
     `.\\venv\\Scripts\\Activate`
   - On Linux/MacOS:
     `source venv/bin/activate`

3. **Install the required dependencies:**
```bash
   pip install -r requirementsOld.txt  # or pythonX.XX -m pip install -r requirementsOld.txt
```
4. **Run the project:**
```bash
   python test.py  # You can rename test.py
```
## How to Install

1. Open Command Prompt and navigate to your desired directory:
    ```bash
    cd your/path
    ```

2. Clone the repository:
    ```bash
    git clone https://github.com/DragoonT/Custom-Status-for-Open-Application.git your_folder_name
    ```
    Or download the [Custom-Status-for-Open-Application.zip](https://github.com/DragoonT/Custom-Status-for-Open-Application/archive/refs/heads/main.zip) to your PC and extract it.

3. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application (Create Bot Discord).
    ![Star_Rail](Star_Rail.png)

4. Click your new application and go to **General Information** to get the **APPLICATION ID** (Client ID) and **Bot** section to get the **TOKEN**.

5. (Optional) To change your bot name, go to **General Information** and edit the bot name for the status to show "Playing your_bot_name".

6. Open `your_file.py` (e.g., `test.py`) and paste **TOKEN**, **CLIENT ID**, **EXECUTABLE_NAME**, yourapplication.exe, and **small_image**.

7. In Visual Studio Code, open the terminal and navigate to your project directory:
    ```bash
    cd path/to/your_folder_name
    ```
    If your folder name is `Custom_Playing_Status_for_Open_Application`, use:
    ```bash
    cd path/to/Custom_Playing_Status_for_Open_Application
    ```

8. Follow the steps in `howtoactivate.txt` or continue with these steps.

9. Install required Python packages:
    ```bash
    pip install discord.py psutil pypresence pillow
    ```

10. Run your script:
    ```bash
    python your_file.py
    ```

11. If the above step fails, follow these commands:
    ```bash
    python -m venv myenv
    myenv\Scripts\activate
    pip install discord.py psutil pypresence pillow
    python your_file.py
    ```

12. Open your application and check the playing status.

    ![app_no_image](app_no_image.png)

## Adding an Image to Your Playing Status

1. Stop the script using Ctrl + C or close the terminal.

2. Add your image to your project folder.

3. Open `cropimage.py` (or rename this file) and set `image_path` to your image's path and `output_path` for the cropped image.

4. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and navigate to **Rich Presence** > **Rich Presence Assets**. Click **Add Image(s)** to upload your cropped image and copy the image name to `small_image="YourRichPresenceAssets"` in `your_file.py`.

    ![richpresenceassets](richpresenceassets.png)

5. If you need to re-upload the image, wait 10-15 minutes and reload the website.

6. Run your script again to see the updated playing status:
    ```bash
    python your_file.py
    ```

    ![app](app.png)

## How to Create and Run the Executable

1. Follow the steps in `howtoactivate.txt` or continue with these steps.

2. Open the terminal, navigate to your project directory, and install PyInstaller:
    ```bash
    pip install pyinstaller
    ```

3. Add your `your_icon.ico` file to your project directory.

4. To create the executable, run:
    ```bash
    pyinstaller --onefile --icon=your_icon.ico your_file.py
    ```
    To create the executable without showing the console, run:
    ```bash
    pyinstaller --onefile --icon=your_icon.ico --noconsole your_file.py
    ```

5. Go to the `dist` directory to find your executable.

    ![exe](exe.png)

## Running on Android (Using Termux or Winlator)

### Requirements
1. [Download Termux](https://github.com/termux/termux-app) (F-Droid recommended) or [Winlator](https://github.com/brunodev85/winlator) to run your Python script on an Android device.

2. (Optional) Install a File Manager app to help navigate project files.

### Steps to Run on Termux

1. **Install Python and Git in Termux**: Open Termux and install the required packages:
    ```shell
    pkg update
    pkg install python git
    ```

2. **Clone the Repository**: Use `cd` to navigate to your desired directory in Termux, then clone the repository:
    ```shell
    cd /path/to/your/folder
    git clone https://github.com/DragoonT/Custom-Status-for-Open-Application.git
    ```

3. **Navigate to the Project Folder**:
    ```shell
    cd Custom-Status-for-Open-Application
    ```

4. **Install Required Python Packages**:
    ```shell
    pip install discord.py psutil pypresence pillow
    ```

5. **Edit** `your_file.py` **to Configure TOKEN, CLIENT ID, EXECUTABLE_NAME, and small_image**:
   Open the script in a text editor (such as Vim, Nano, or any other Termux-compatible editor), and input your Discord bot TOKEN, CLIENT ID, EXECUTABLE_NAME, and small_image.

6. **Run Your Script**:
    ```shell
    python your_file.py
    ```

### Steps to Run on Winlator

**Winlator** is an emulator that allows running Windows applications on Android devices. Here’s how to set it up:

1. **Download and Install Winlator**:
   Follow the instructions on [Winlator's GitHub](https://github.com/brunodev85/winlator) to set it up on your device.

2. **Transfer Your Project Files to the Winlator Directory**:
   Place your Python project in a folder accessible to Winlator.

3. **Configure Python in Winlator**:
   Install Python for Windows within Winlator if it’s not already included.

4. **Run Your Script**:
    ```shell
    python your_file.py
    ```

**Note:** Performance may vary depending on the Android device specifications.

### Adding an Image on Android
1. Follow the steps above to add an image to your project directory.
2. You can upload images to Discord Rich Presence Assets as explained in the earlier section, and link it in `small_image="YourRichPresenceAssets"` in `your_file.py`.

## How to Use the Pre-Built `.exe` on Android

If you're an Android user and want to run the `.exe` file directly, you can use an Android app that emulates a Windows environment. **Winlator** is a popular choice that allows you to run Windows applications, including `.exe` files, on Android.

### Requirements
1. Download **Winlator** (or similar app) from [Winlator's GitHub page](https://github.com/brunodev85/winlator) or an alternative source.
2. A file manager app is recommended to help navigate project files on your Android device.

### Alternative Option: Using ExaGear (Older Android Devices)

**ExaGear** is another Android app that emulates Windows environments but may not work on all Android versions, as it is no longer actively supported. For older devices, however, it might be an alternative if Winlator does not perform as expected.

1. Download and install ExaGear on your device.
2. Follow similar steps as above to load and run `CustomStatusDiscord.exe`.

**Note**: Performance may vary depending on your device's specifications. Winlator typically requires devices with higher RAM and processing power for smooth emulation.
