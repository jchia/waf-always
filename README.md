# waf-always
Test case for demoing waf bug

revision.hpp is generated for the 'revision' target by running a custom command specified in the wscript and contains the current git commit hash. Other targets are supposed to depend on it, including the 'test' target.

There is a deliberate `sleep 10` for the "revision" target to make the console output clearly show the order of relevant build events.

The bug is that the 'test' target does not respect the dependency. Sometimes, when building, test.cpp gets built before the 'revision' target finishes building or does not get built at all.

I suspect that waf does not dependency-track files in symlinked directories the way I want for; i.e. just like normal files.

The problem shows up in the initial commit, i.e. 922fdc1f9e2e4997913a643f46ae6334e16af376 but seems to go away in the second commit, i.e. 30104b838df6547db4189027d9892ce73710f376, where I use a file symlink for revision.hpp instead of a directory symlink for the directory containing revision.hpp.
