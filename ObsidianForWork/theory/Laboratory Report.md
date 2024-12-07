### Laboratory Report: Simple Control System Design with PID Controller for DC Motor

#### Objective:

The goal of this laboratory work is to design and analyze a simple control system for a **DC Motor** using **PID (Proportional-Integral-Derivative) control**. The objective was to investigate the behavior of the motor under both **open-loop** and **closed-loop** control systems and observe the impact of different PID gains on system performance.

---

### 1. **System Overview**

The system consists of a **DC motor** with a simple transfer function where the input is the **voltage** and the output is the **RPM (Revolutions Per Minute)** of the motor. The motor's transfer function is given as:

1s+10+10−5\frac{1}{s + 10 + 10^{-5}}

This transfer function is used in both the open-loop and closed-loop control systems. The PID controller adjusts the output based on the error between the desired RPM and the actual RPM.

---

### 2. **Simulation Setup**

The following blocks were used to simulate the system in **Xcos** (a Scilab graphical simulator):

- **Transfer Function (CLR)**: Represents the DC motor's dynamics.
- **Step Function**: To provide a step input for the system.
- **SUMf**: To calculate the error signal between the desired and actual output.
- **PID**: A proportional-integral-derivative controller to adjust the motor's speed.
- **Gain**: Used to adjust certain parameters in the system.
- **CMScope**: Used to visualize the system's response.
- **Clock**: To simulate real-time operation.

---

### 3. **Open-Loop System**

In the **open-loop system**, the motor operates without any feedback. The system was modeled as follows:

- **Input**: Step function (step input to the motor).
- **Output**: Motor's RPM (simulated without feedback).

The system behavior was observed without any corrective actions, meaning the motor's RPM was solely determined by the input voltage.

---

### 4. **Closed-Loop System**

In the **closed-loop system**, feedback is used to correct the motor's RPM. The output is compared with the desired RPM, and the difference (error) is used to adjust the motor's speed through a PID controller.

- **PID Controller**: Initially set with gains P=1,I=1,D=1P = 1, I = 1, D = 1.

In this system, the error signal is continuously fed back into the controller, allowing it to adjust the motor’s voltage and achieve the desired output.

---

### 5. **PID Tuning**

The initial PID gains were set to P=1,I=1,D=1P = 1, I = 1, D = 1. The system's response to a step input was observed, as shown in **Figure 9** (response with PID gains = [1, 1, 1]).

After several trials and adjustments, the PID gains were optimized to:

- **New PID Gains**: P=28,I=19,D=0.5P = 28, I = 19, D = 0.5.

With these new PID gains, the closed-loop system showed a significant improvement in performance, reducing the error and achieving a stable RPM more quickly.

---

### 6. **Results**

- **Open-Loop Response**: Without feedback, the motor’s RPM followed the input step function but had a larger error and instability.
    
- **Closed-Loop Response**: With the optimized PID gains, the motor’s RPM quickly converged to the desired value, demonstrating the effectiveness of feedback control. The error was minimized, and the system stabilized at the target RPM.
    
    - **New PID Gains**: P=28,I=19,D=0.5P = 28, I = 19, D = 0.5.
    - The system now shows a small steady-state error with much faster convergence, as shown in **Figure 11** (response with optimized PID gains).

---

### 7. **Conclusion**

This experiment demonstrated the importance of feedback control in regulating the speed of a DC motor. By tuning the PID controller, the system was able to minimize error and achieve a stable output with minimal delay. The results clearly show the impact of PID gains on the motor’s behavior, with proper tuning resulting in faster and more accurate system responses.

The success of the closed-loop system with optimized PID gains emphasizes the importance of careful controller design in practical control systems.
