Your repository structure is neatly set up with three core modules corresponding to the projects:

1. **`indian-route-map-main/`** — India Road Network Navigation (Dijkstra's / UCS)


2. **`Unmanned-Ground-Vehicle-Static--main/`** — Static Battlefield UGV Pathplanning & MoEs


3. **`Unmanned-Ground-Vehicle-Dynamic--main/`** — Dynamic/Unknown Obstacle UGV Navigation



---

### Quick Tip for Cleanliness

Notice how your folders have nested subfolders (e.g., `indian-route-map-main/indian-route-map-main`) because of GitHub uploads from extracted ZIP files. If you want a cleaner repository URL and navigation, you can move the contents directly into the main project root or rename the folders to simpler names like `indian-route-map`, `ugv-static`, and `ugv-dynamic`.

---

### Updated Root `README.md`

Here is a customized root README tailored precisely to your repository structure so that visitors can easily navigate into each folder:

```markdown
# AI Projects Suite

> Advanced pathplanning, Uniform-Cost Search (Dijkstra's Algorithm), and adaptive real-time navigation for Unmanned Ground Vehicles (UGVs) and road networks.

---

## 📂 Repository Structure

| Module | Directory | Description |
| :--- | :--- | :--- |
| **1. India Road Network** | [`indian-route-map-main/`](./indian-route-map-main) | Implements Uniform-Cost Search (Dijkstra's algorithm) across major Indian cities using real road distance matrices. |
| **2. Static UGV Navigation** | [`Unmanned-Ground-Vehicle-Static--main/`](./Unmanned-Ground-Vehicle-Static--main) | Battlefield pathplanning on a $70\times70\text{ km}$ grid across three obstacle density levels with Measures of Effectiveness (MoEs). |
| **3. Dynamic UGV Navigation** | [`Unmanned-Ground-Vehicle-Dynamic--main/`](./Unmanned-Ground-Vehicle-Dynamic--main) | Real-time adaptive replanning for moving and unknown obstacles using incremental heuristic search. |

---

## 🚀 Getting Started

Clone the repository and explore individual project directories:

```bash
git clone [https://github.com/revanthkrishnasai00/AI_Projects.git](https://github.com/revanthkrishnasai00/AI_Projects.git)
cd AI_Projects

```

Navigate into any module folder to find its respective source code, datasets, and execution instructions.

```
