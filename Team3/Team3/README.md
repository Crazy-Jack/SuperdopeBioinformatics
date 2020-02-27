 # Instructions on how to work together integrating all softwares

Two files you have to modify:
- `__main__.py`
- `yoursubprocessname.py`

Inside `__main__.py`:
- First, in the SECTION 1, I already defined input and output filename and the intermediate file folder. You don't need to worry about them. 

- Second, in the SECTION 2, we have to define the specific parameter needed by different subprograms. The way argparse works is that when using `-xxx SOMETHING` in the command line, we can get the argument `ABC` by calling `args.xxx`. Different settings like `action` may results in different data structures. You can define whatever way you want and retrive them in section 3. More information can be found here: https://docs.python.org/3/library/argparse.html

- Third, in SECTION 3, we need to retrieve the arg parameters and pass them into the class we created in our seperated module. Follow the example of PureClip and you can define whatever names of parameters you want. But be sure be consistent with the input and output filename which may be used in other upsteam or downsteam programs.


Inside each `module.py`:
- Retrieve your the parameters at `__init__()` function.
- Based on your logic of the command, synthesize and run the command
- Note that you only have to concate your command into `command` variable. 


Another thing to note is that since we may want to jointly modify the same `__main__.py` file, we need work on different branches first and then you can do pull request to merge to the master. If you wish to use output file from upstream, be sure to write a comment about what is this file so at the end I can unify the variables. 

By doing the above, we are done XD! It would be interesting to see if this mode is efficient or not. Pin me for questions. 



