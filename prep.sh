#!/bin/bash
# python-awips prep script
# author: mjames@ucar.edu
#

# should be /awips2/repo/python-awips or ~/python-awips
dir="$( cd "$(dirname "$0")" ; pwd -P )"

# Find plugin-contributed files and add them to the site packages.
find /awips2/repo/awips2-core/common/ -path '*/pythonPackages/dynamicserialize' \
   -exec cp {} -rv ${dir} \;
find /awips2/repo/awips2-builds/edexOsgi/ -path '*/pythonPackages/dynamicserialize' \
   -exec cp {} -rv ${dir} \;

#bash %{_baseline_workspace}/build.edex/opt/tools/update_dstypes.sh %{_build_root}/awips2/python/lib/python2.7/site-packages/dynamicserialize

# Update __init__.py files under dynamicserialize/dstypes/ to include
# all contributed python packages and modules within __all__ in the packages'
# __init__.py

echo "Updating dynamicserialize/dstypes"
# Update __all__  for every package under dstypes
for package in $(find dynamicserialize/dstypes -name __init__.py -printf '%h ')
do
    pushd $package > /dev/null
    # find non-hidden packages
    subpackages=$(find . -maxdepth 1 -type d ! -name ".*" -printf '%f\n' | sort)

    # find non-hidden python modules
    modules=$(find . -maxdepth 1 -type f \( -name "*.py" ! -name "__init__.py" ! -name ".*" \) -printf '%f\n' | sed 's/\.py//' | sort)

    # join subpackages and modules into a single list, modules first
    all=("${subpackages[@]}" "${modules[@]}")
    joined=$(printf ",\n            \'%s\'" "${all[@]}")

    #replace the current __all__ definition with the rebuilt __all__, which now includes all contributed packages and modules.
    #-0777 allows us to match the multi-line __all__ definition
    perl -0777 -p -i -e "s/__all__ = \[[^\]]*\]/__all__ = \[$(echo \"${joined:1}\")\n          \]/g" __init__.py

    popd > /dev/null
done
echo "Done"

#find ${dir} -type f | xargs sed -i 's/[ \t]*$//'
git grep -l 'ufpy' | xargs sed -i 's/ufpy/awips/g'

#find ${dir} -type f | xargs sed -i '/# This software was developed and \/ or modified by Raytheon Company,/,/# further licensing information./d'



# update import strings for python3 compliance


