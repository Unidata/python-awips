#!/bin/bash
# python-awips prep script
# author: mjames@ucar.edu
# author: tiffanym@ucar.edu

# This script scrapes the awips2 repos for dynamicserialize, thrift, and awips to package them for python-awips

# should be /awips2/repo/python-awips or ~/python-awips
dir="$( cd "$(dirname "$0")" ; pwd -P )"
echo $dir
rm -rf ${dir}/src

# Find plugin-contributed files and add them to the site packages.
mkdir -p ${dir}/src/dynamicserialize

find /awips2/repo/awips2-core/common/ -path '*/pythonPackages/dynamicserialize' \
   -exec cp {} -rv ${dir}/src \;
find /awips2/repo/awips2-hazards/common/ -path '*/pythonPackages/dynamicserialize' \
   -exec cp {} -rv ${dir}/src \;
find /awips2/repo/awips2/ -path '*/pythonPackages/dynamicserialize' \
   -exec cp {} -rv ${dir}/src \;

#bash %{_baseline_workspace}/build.edex/opt/tools/update_dstypes.sh %{_build_root}/awips2/python/lib/python2.7/site-packages/dynamicserialize

# Update __init__.py files under dynamicserialize/dstypes/ to include
# all contributed python packages and modules within __all__ in the packages'
# __init__.py

echo "Updating dynamicserialize/dstypes"
# Update __all__  for every package under dstypes
for package in $(find src/dynamicserialize/dstypes -name __init__.py -printf '%h ')
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

#################
# Updating ufpy
#################
mkdir -p ${dir}/src/awips
cp -r /awips2/repo/awips2/pythonPackages/ufpy/* ${dir}/src/awips/

# Replace all instances of ufpy with awips
rg -l -0 'ufpy' -- src/ | xargs -0 sed -i 's/ufpy/awips/g'
###################
# Updating thrift  
###################
mkdir -p ${dir}/src/thrift

find /awips2/repo/awips2-core/ -path '*/bin/*/serialization/thrift' \
   -exec cp {} -rv ${dir}/src \;


find /awips2/repo/awips2-rpm -name 'thrift*gz' \
    -exec tar -xzf {} \
    -C "${dir}/src/thrift/" \
    --strip-components=4 \
    thrift-0.18.1/lib/py/src/ \;

rm -rf ${dir}/src/thrift/ext

# These are files that are Unidata specific and need to be restored
git restore ${dir}/src/awips/RadarCommon.py
git restore ${dir}/src/awips/dataaccess/ModelSounding.py
git restore ${dir}/src/awips/tables.py
git restore ${dir}/src/dynamicserialize/dstypes/com/raytheon/uf/common/datastorage/records/AbstractDataRecord.py

# These are files that Unidata made changes to and most likely we will want to keep our changes - most likely none of these files have changed by NWS
git restore ${dir}/src/awips/dataaccess/DataAccessLayer.py
git restore ${dir}/src/awips/dataaccess/ThriftClientRouter.py
git restore ${dir}/src/awips/gfe/IFPClient.py
git restore ${dir}/src/dynamicserialize/dstypes/com/raytheon/uf/common/auth/user/UserId.py
git restore ${dir}/src/dynamicserialize/dstypes/com/raytheon/uf/common/dataplugin/gfe/db/objects/GFERecord.py
git restore ${dir}/src/dynamicserialize/dstypes/com/raytheon/uf/common/dataplugin/gfe/db/objects/ParmID.py
git restore ${dir}/src/dynamicserialize/dstypes/com/raytheon/uf/common/dataplugin/level/Level.py
git restore ${dir}/src/dynamicserialize/dstypes/com/raytheon/uf/common/dataquery/requests/RequestConstraint.py
git restore ${dir}/src/dynamicserialize/dstypes/com/raytheon/uf/common/dataplugin/level/MasterLevel.py
git restore ${dir}/src/dynamicserialize/dstypes/com/raytheon/uf/common/localization/LocalizationLevel.py
git restore ${dir}/src/dynamicserialize/dstypes/com/raytheon/uf/common/message/WsId.py
git restore ${dir}/src/dynamicserialize/dstypes/java/util/EnumSet.py
