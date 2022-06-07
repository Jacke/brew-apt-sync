from abc import ABC, abstractmethod

from package_repr import PackageRepr
from typing import (
    List
)

class PackageMappers:
  def map(platforms: List[str]):
    for platform in platforms:
      print(platform)
    
  def brewfile(packages: List[PackageRepr]):
    pass
  def aptfile(packages: List[PackageRepr]):
    pass  