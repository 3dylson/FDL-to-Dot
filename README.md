# A parser and a translator from FDL (Feature Description Language) to DOT Language (GraphViz)

The idea is to receive a FDL specification
and generate a diagram of that specification built in dot to be visualized in
GraphViz.

## Feature Diagram for bicycle

![image](https://github.com/3dylson/FDL-to-Dot/blob/main/graphviz.png)


## Textual equivalent of feature diagrams

```
Bicycle : all (Frame, Gear, opt (Accessory))
Frame : one-of (small, medium, big)
Gear : one-of (18, 24)
Accessory : more-of (light, bell)
```
