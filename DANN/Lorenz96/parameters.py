F = 8
J = 40
step_size       = 0.05     # 积分步长（相当于6小时）
da_interval     = 4        # 同化时间间隔（相当于1天）
window_len      = 200      # 同化窗口长度（相当于50天）
background_err  = 0.0      # 先验场的参数误差
relative_err    = 2.9e-2
# background_err  = 1.5      # 先验场的参数误差
# relative_err    = 5.4e-3
# background_err  = 2.5      # 先验场的参数误差
# relative_err    = 1.4e-2
# background_err  = 3.0      # 先验场的参数误差
# relative_err    = 2.1e-2
NbTraining      = 2000    # 训练集大小
NbVal           = 300     # 验证集大小
NbTest          = 200     # 测试集大小
sigNoise        = 1.414    # 观测噪声标准差