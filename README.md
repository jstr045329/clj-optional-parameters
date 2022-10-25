# clj-optional-parameters
Generate skeletons for Clojure functions with optional parameter maps.
<br>
<br>This Python script takes command line parameters like this:
<br>  $ python generate_optional_parameters.py my-function-name optional-param-1 99 optional-param-2 42 and outputs something like this:

<br>&nbsp;&nbsp;(defn my-function-name [your-args-here param-map]
<br>&nbsp;&nbsp;&nbsp;&nbsp;(let [optional-param-1 (if (:optional-param-1 param-map) (:optional-param-1 param-map) 99)
<br>&nbsp;&nbsp;optional-param-2 (if (:optional-param-2 param-map) (:optional-param-2 param-map) 42)]
<br>&nbsp;&nbsp;()) ;; Your code here

<br>In other words, Clojure will check for the presence of each optional key in param-map. If the key is present, 
its associated value will be used. Otherwise, some deefault that you passed Python in the command line will be used.

<br>This way, the work that goes into creating and maintaining functions with optional parameters is greatly reduced.
