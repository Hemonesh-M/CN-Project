# 📁 Peer-to-Peer File Sharing System

A simple BitTorrent-style peer-to-peer (P2P) file sharing system built using Python and socket programming. This system allows peers to register files with a central tracker and download files directly from each other.

---

## 🎬 Demo

📺 [Watch Demo on YouTube](https://youtu.be/qpsYcf7ZK3A)  


---

## 🚀 Features

- Centralized tracker to manage file-to-peer mappings.
- File registration (seeding).
- File downloading from other peers (leeching).
- Peer discovery via tracker.
- Works on the same machine or across devices on the same network.

---

## 🗂️ Folder Structure

p2pFileSharing/  
├── tracker_server.py    # Central tracker server  
├── peer.py              # Peer logic (seed / download)  
├── filesA/             # Peer A's folder (contains the original shared files)  
│   └── cat.jpg          # Example file to share  
├── filesB/             # Peer B's folder (receives the downloaded files)  
└── README.md           # This documentation  


---

## 🛠️ How to Run

**Step 1: Start the Tracker (on one machine)**

1.  Open your terminal or command prompt.
2.  Navigate to the `p2pFileSharing` directory.
3.  Run the following command:

    ```bash
    python tracker_server.py
    ```

    *The tracker will start listening on port 8000.*

**Step 2: Start Peer A (Seeder)**

1.  Open another terminal or command prompt.
2.  Navigate to the `p2pFileSharing` directory.
3.  Run the following command:

    ```bash
    python peer.py
    ```

4.  Follow the prompts:

    ```
    Enter port: 9001
    Folder path: ./filesA
    Register file: cat.jpg
    ```

    *Peer A is now seeding `cat.jpg`.*

**Step 3: Start Peer B (Leecher)**

1.  Open another terminal or command prompt (or use the same machine if you prefer).
2.  Navigate to the `p2pFileSharing` directory.
3.  Run the following command:

    ```bash
    python peer.py
    ```

4.  Follow the prompts:

    ```
    Enter port: 9002
    Folder path: ./filesB
    ```

5.  Choose the option to download `cat.jpg` from the menu.

    *Peer B will attempt to download `cat.jpg` from Peer A.*

    *After the download completes, the `cat.jpg` file will be located in the `filesB/` folder.*
