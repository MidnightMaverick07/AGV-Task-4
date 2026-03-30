# ViZDoom Autonomous Navigation

## Overview

This project focuses on building an autonomous navigation system in a custom ViZDoom maze.

The system performs global path planning using RRT* and follows the path using a feedback controller. The main challenge was not just finding a path, but executing it reliably in a constrained environment.

---

## Objective

- Plan a path from start to goal using the automap  
- Navigate the agent using a controller  
- Avoid obstacles and handle corner cases  
- Ensure stable movement without getting stuck  

---

## System Pipeline

```
Automap → Map Processing → RRT* → Path Smoothing → Controller
```

---

## Approach

### 1. Map Extraction

- Used `automap_buffer` to extract the maze  
- Converted image into a binary occupancy grid  
- Identified:
  - Free space  
  - Walls  
  - Start and goal  

---

### 2. Map Processing

- Initial thresholding caused incorrect classification  
- Applied a **two-step approach**:

**Step 1:** Loose threshold to maintain connectivity  
**Step 2:** Distance transform to enforce safety margin  

This ensured:
- Path exists  
- Agent stays away from walls  

---

### 3. Path Planning (RRT*) 

- Implemented RRT* from scratch  
- Features:
  - Random sampling with goal bias  
  - Collision checking  
  - Rewiring for optimal path  

**Key Parameters:**
- Iterations: 30,000  
- Step size: 8  
- Goal bias: 20%  

---

### 4. Path Smoothing

- Raw RRT* paths were jagged  
- Filtered closely spaced waypoints  
- Reduced sharp turns  

---

### 5. Controller

- Computes angle to next waypoint  
- Controls:
  - Turning (left/right)  
  - Forward movement  

**Logic:**
- Large angle → rotate  
- Small angle → move forward  

---

### 6. Stuck Detection & Recovery

Major issue: agent getting stuck in corners.

**Solution:**
- Track position over time  
- If movement is too small → detect stuck  

**Recovery Strategy:**
- Phase 1: move backward  
- Phase 2: rotate  

This prevents infinite loops.

---

## Key Challenges and Fixes

### 1. Agent Stuck in Corners
**Fix:** Added stuck detection + recovery  

### 2. Infinite Back-and-Forth Loop
**Fix:** Added rotation after backward motion  

### 3. Path Through Walls
**Fix:** Improved map thresholding  

### 4. Broken Connectivity
**Fix:** Used distance transform  

### 5. Narrow Passage Failure
**Issue:** RRT* struggles in tight spaces  
**Status:** Still partially unresolved  

---

## Results

- Successfully generates a path using RRT*  
- Agent follows path with reasonable stability  
- Handles most corner cases  
- Still struggles in very narrow passages  

---

## Key Learnings

- Planning alone is not enough — control matters equally  
- Map quality directly affects path validity  
- RRT* struggles with narrow corridors  
- Recovery mechanisms are essential  

---

## Tech Stack

- Python  
- OpenCV  
- ViZDoom  

---

## Output

- Path visualization (`path_level1.png`)  
- Agent trajectory video  
- Processed occupancy map  

---

## Future Improvements

- Replace RRT* with A* for grid-based planning  
- Improve controller with obstacle awareness  
- Better handling of narrow passages  

---

## Author

Subhojeet Ghosh

---

If you found this useful, feel free to star the repo.
