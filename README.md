# clj-optional-parameters
Generate skeletons for Clojure functions with optional parameter maps.

This Python script takes command line parameters like this:
  $ python generate_optional_parameters.py my-function-name optional-param-1 99 optional-param-2 42
and outputs something like this:

  (defn my-function-name [your-args-here param-map]
    (let [optional-param-1 (if (:optional-param-1 param-map) (:optional-param-1 param-map) 99)
          optional-param-2 (if (:optional-param-2 param-map) (:optional-param-2 param-map) 42)]
    ()) ;; Your code here

In other words, Clojure will check for the presence of each optional key in param-map. If the key is present, 
its associated value will be used. Otherwise, some deefault that you passed Python in the command line will be used.

This way, the work that goes into creating and maintaining functions with optional parameters is greatly reduced.
