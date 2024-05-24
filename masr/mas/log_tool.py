# logs
# 记录类属性变化

from loguru import logger

def log_changes(*attrs):
    def decorator(cls):
        original_setattr = cls.__setattr__

        def new_setattr(self, name, value):
            if name in attrs and hasattr(self, name) and getattr(self, name) != value:
                logger.info(f"Attribute: 【'{name}'】; new value: 【{value}】")
            original_setattr(self, name, value)
        
        cls.__setattr__ = new_setattr
        return cls
    return decorator

# # 应用装饰器到类 A
# @log_changes('grass')
# class A:
#     def __init__(self, grass, tree):
#         self.grass = grass
#         self.tree = tree

# # 应用装饰器到类 B
# @log_changes('bottle', 'water')
# class B:
#     def __init__(self, bottle, water, cup):
#         self.bottle = bottle
#         self.water = water
#         self.cup = cup