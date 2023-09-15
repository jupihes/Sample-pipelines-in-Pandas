
## Preparing graph
https://people.duke.edu/~ccc14/sta-663-2018/notebooks/S10B_MarkovChains.html


### using `dot` 
```dot
digraph g {
    node [shape=circle]
    R [label="Rainy"]
    S [label="sunny"]
    C [label="Cloudy"]
    R -> R [label=0.6]
    R -> C [label=0.3]
    R -> S [label=0.1]
    C -> R [label=0.5]
    C -> C [label=0.1]
    C -> S [label=0.4]
    S -> R [label=0.1]
    S -> C [label=0.4]
    S -> S [label=0.5]
}
```

## command to convert

- In Windows commandline
```shell
dot -Tpng input.dot > input.png
```
