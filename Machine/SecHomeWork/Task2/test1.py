import io
import keras
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D

# 下面几行调整报告的粒度。
# 设置Pandas DataFrame 或 Series 在显示时最多显示的行数为 10。这在处理大型数据集时很有用，可以确保输出不会太长，方便查看数据的一部分而不是整个数据集。
pd.options.display.max_rows = 10

# 设置Pandas 显示浮点数时的格式。在这里，"{:.1f}".format 表示浮点数将以一位小数的格式显示。这样可以控制浮点数的显示精度，使输出更易读。
pd.options.display.float_format = "{:.1f}".format
print("Ran the import statements.")

# 数据存储
rice_dataset_raw = pd.read_csv(
    "https://download.mlcc.google.com/mledu-datasets/Rice_Cammeo_Osmancik.csv"
)

# 特定列
rice_dataset = rice_dataset_raw[
    [
        "Area",  # 面积
        "Perimeter",  # 周长
        "Major_Axis_Length",  # 主轴长
        "Minor_Axis_Length",  # 小轴长
        "Eccentricity",  # 离心率
        "Convex_Area",  # 凸区域
        "Extent",  # 范围
        "Class",  # 种类
    ]
]

# 生成关于rice_dataset DataFrame 中数值列的统计摘要。这包括计数、均值、标准差、最小值、25% 分位数、中位数、75% 分位数和最大值等信息。
rice_dataset.describe()
print(
    f"主长度最短 {rice_dataset.Major_Axis_Length.min():.1f}px,"
    f"主长度最长 {rice_dataset.Major_Axis_Length.max():.1f}px"
    "\n"
    f"面积最小 {rice_dataset.Area.min()}px,"
    f"面积最大 {rice_dataset.Area.max()}px"
    "\n"
    "稻谷最大周长"
    f" {rice_dataset.Perimeter.max():.1f}px, 约"
    f" ~{(rice_dataset.Perimeter.max() - rice_dataset.Perimeter.mean())/rice_dataset.Perimeter.std():.1f} 标准差"
    f"  ({rice_dataset.Perimeter.std():.1f}) 距离平均数"
    f" ({rice_dataset.Perimeter.mean():.1f}px)."
    "\n"
    f"计算公式为: ({rice_dataset.Perimeter.max():.1f} -"
    f" {rice_dataset.Perimeter.mean():.1f})/{rice_dataset.Perimeter.std():.1f} ="
    f" {(rice_dataset.Perimeter.max() - rice_dataset.Perimeter.mean())/rice_dataset.Perimeter.std():.1f}"
)

# 打一个网页出来
#   for x_axis_data, y_axis_data in [
#     ('Area', 'Eccentricity'),
#     ('Convex_Area', 'Perimeter'),
#     ('Major_Axis_Length', 'Minor_Axis_Length'),
#     ('Perimeter', 'Extent'),
#     ('Eccentricity', 'Major_Axis_Length'),
# ]:
#   px.scatter(rice_dataset, x=x_axis_data, y=y_axis_data, color='Class').show()


# # 颜色映射字典
# color_map = {'Cammeo': 'red', 'Osmancik': 'blue'}
# #创建5个相互对应的2D特征图，按类别进行颜色编码。
# for x_axis_data, y_axis_data in [
#     ('Area', 'Eccentricity'),
#     ('Convex_Area', 'Perimeter'),
#     ('Major_Axis_Length', 'Minor_Axis_Length'),
#     ('Perimeter', 'Extent'),
#     ('Eccentricity', 'Major_Axis_Length'),
# ]:
#     # 获取对应的颜色值
#     colors = [color_map[c] for c in rice_dataset['Class']]
#     # 绘制散点图
#     plt.scatter(rice_dataset[x_axis_data], rice_dataset[y_axis_data], c=colors)

#     # 添加标题和轴标签
#     plt.title(f'Scatter Plot of {x_axis_data} vs {y_axis_data}')
#     plt.xlabel(x_axis_data)
#     plt.ylabel(y_axis_data)

#     # 显示图形
#     plt.show()
# 颜色映射字典
color_map = {"Cammeo": "red", "Osmancik": "blue"}

# 创建一个包含5个子图的图形
fig, axes = plt.subplots(1, 5, figsize=(15, 3))

# 遍历不同的x轴和y轴数据对
for i, (x_axis_data, y_axis_data) in enumerate(
    [
        ("Area", "Eccentricity"),
        ("Convex_Area", "Perimeter"),
        ("Major_Axis_Length", "Minor_Axis_Length"),
        ("Perimeter", "Extent"),
        ("Eccentricity", "Major_Axis_Length"),
    ]
):
    # 获取对应的颜色值
    colors = np.array([color_map[c] for c in rice_dataset["Class"]])

    # 在当前子图中绘制散点图
    axes[i].scatter(rice_dataset[x_axis_data], rice_dataset[y_axis_data], c=colors)

    # 添加标题和轴标签
    axes[i].set_title(f"{x_axis_data} vs {y_axis_data}")
    axes[i].set_xlabel(x_axis_data)
    axes[i].set_ylabel(y_axis_data)

# 调整子图之间的间距
plt.tight_layout()

# 显示图形
# plt.show()


"""**************************3D图像*****************************"""
# px.scatter_3d(
#     rice_dataset,
#     x='Eccentricity',
#     y='Area',
#     z='Major_Axis_Length',
#     color='Class',
# ).show()

# 颜色映射字典
color_map = {"Cammeo": "red", "Osmancik": "blue"}

# 创建一个三维图形
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# 设置x轴、y轴和z轴的数据
x_axis_data = rice_dataset["Eccentricity"]
y_axis_data = rice_dataset["Area"]
z_axis_data = rice_dataset["Major_Axis_Length"]

# 获取对应的颜色值
colors = np.array([color_map[c] for c in rice_dataset["Class"]])

# 绘制三维散点图
ax.scatter(x_axis_data, y_axis_data, z_axis_data, c=colors)

# 添加标题和轴标签
ax.set_title("3D Scatter Plot")
ax.set_xlabel("Eccentricity")
ax.set_ylabel("Area")
ax.set_zlabel("Major_Axis_Length")

# 显示图形
# plt.show()
"""**************************Z 分数规范化*****************************"""
# 将大米数据集中的数值转换为 Z 分数来对其进行规范化。
# Z 分数是该值与平均值之间的标准差。
# 考虑一个平均值为 60、标准差为 10 的特征。
# 原始值 75 的 Z 分数为 +1.5： Z-score = (75 - 60) / 10 = +1.5
# 原始值 38 的 Z 分数为 -2.2： Z-score = (38 - 60) / 10 = -2.2
# 计算了 rice_dataset 数据集中数值特征的平均值。numeric_only=True 参数用于仅计算数值列的平均值。
feature_mean = rice_dataset.mean(numeric_only=True)
# 计算了 rice_dataset 数据集中数值特征的标准差。同样，numeric_only=True 参数用于仅计算数值列的标准差。
feature_std = rice_dataset.std(numeric_only=True)
# 选择了 rice_dataset 数据集中的数值列，并将其列名存储在 numerical_features 变量中。select_dtypes('number') 用于选择数值类型的列。
numerical_features = rice_dataset.select_dtypes("number").columns
# 创建了一个新的 DataFrame normalized_dataset，其中包含了经过规范化处理的数值特征。它使用了先前计算的平均值和标准差来计算每个数值特征的 z 分数。通过将每个数值特征减去平均值，然后除以标准差，可以将特征值转换为 z 分数
normalized_dataset = (rice_dataset[numerical_features] - feature_mean) / feature_std
# 将原始数据集中的 'Class' 列复制到新的规范化数据集中。
normalized_dataset["Class"] = rice_dataset["Class"]
# 打印出规范化后的数据集的前几行，以便检查规范化的结果。它显示了规范化后的数值特征，其中大多数 z 分数应该介于 -2 和 +2 之间。
# print(normalized_dataset.head())


"""**************************开始训练*****************************"""
# 为了使实验可重复，我们设置了随机数生成器的种子。这意味着每次运行 colab 时，数据的打乱顺序、随机权重初始化的值等都将相同。
keras.utils.set_random_seed(42)

# 为了训练模型，我们将任意为 Cammeo 物种分配标签“1”，为 Osmancik 物种分配标签“0”。
normalized_dataset["Class_Bool"] = (
    # 如果class是Cammeo返回true，如果class是Osmancik返回false
    normalized_dataset["Class"]
    == "Cammeo"
).astype(int)
# 然后显示10个随机选择的行。
# print(normalized_dataset.sample(10))


# 在第80和90个百分位数处创建指数
number_samples = len(normalized_dataset)  # 计算规范化数据集中的样本数量。
index_80th = round(number_samples * 0.8)  # 算了第80个百分位数的索引位置
index_90th = index_80th + round(
    number_samples * 0.1
)  # 计算了第90个百分位数的索引位置。

# 随机化顺序，并以。8,.1,.1分割为训练，验证和测试
# 打乱样本的顺序
shuffled_dataset = normalized_dataset.sample(frac=1, random_state=100)
train_data = shuffled_dataset.iloc[0:index_80th]  # 选择前80%的样本作为训练数据
validation_data = shuffled_dataset.iloc[
    index_80th:index_90th
]  # 第80%到第90%之间的样本作为验证数据
test_data = shuffled_dataset.iloc[index_90th:]  # 第90%之后的样本作为测试数据。

# 显示最后一次分割的前五行
print(test_data.head())

# 标签的列名列表
label_columns = ["Class", "Class_Bool"]
# 从训练数据集中删除标签列，并将剩余的特征列存储在 train_features 变量中。
train_features = train_data.drop(columns=label_columns)
# 验证数据集中的 'Class_Bool' 列转换为 NumPy 数组，并将其存储在 validation_labels 变量中。
train_labels = train_data["Class_Bool"].to_numpy()

# 从验证数据集中删除标签列，并将剩余的特征列存储在 validation_features 变量中。
validation_features = validation_data.drop(columns=label_columns)
# 将验证数据集中的 'Class_Bool' 列转换为 NumPy 数组，并将其存储在 validation_labels 变量中。
validation_labels = validation_data["Class_Bool"].to_numpy()


# 从测试数据集中删除标签列，并将剩余的特征列存储在 test_features 变量中。
test_features = test_data.drop(columns=label_columns)
# 将测试数据集中的 'Class_Bool' 列转换为 NumPy 数组，并将其存储在 test_labels 变量中。
test_labels = test_data["Class_Bool"].to_numpy()


# Name of the features we'll train our model on.
input_features = [
    "Eccentricity",
    "Major_Axis_Length",
    "Area",
]

# @title Define the functions that create and train a model.

import dataclasses


@dataclasses.dataclass()
class ExperimentSettings:
    """Lists the hyperparameters and input features used to train am model."""

    learning_rate: float
    number_epochs: int
    batch_size: int
    classification_threshold: float
    input_features: list[str]


@dataclasses.dataclass()
class Experiment:
    """Stores the settings used for a training run and the resulting model."""

    name: str
    settings: ExperimentSettings
    model: keras.Model
    epochs: np.ndarray
    metrics_history: keras.callbacks.History

    def get_final_metric_value(self, metric_name: str) -> float:
        """Gets the final value of the given metric for this experiment."""
        if metric_name not in self.metrics_history:
            raise ValueError(
                f"Unknown metric {metric_name}: available metrics are"
                f" {list(self.metrics_history.columns)}"
            )
        return self.metrics_history[metric_name].iloc[-1]


def create_model(
    settings: ExperimentSettings,
    metrics: list[keras.metrics.Metric],
) -> keras.Model:
    """Create and compile a simple classification model."""
    model_inputs = [
        keras.Input(name=feature, shape=(1,)) for feature in settings.input_features
    ]
    # Use a Concatenate layer to assemble the different inputs into a single
    # tensor which will be given as input to the Dense layer.
    # For example: [input_1[0][0], input_2[0][0]]

    concatenated_inputs = keras.layers.Concatenate()(model_inputs)
    dense = keras.layers.Dense(
        units=1,
        input_shape=(1,),
        name="dense_layer",
        activation=keras.activations.sigmoid,
    )
    model_output = dense(concatenated_inputs)
    model = keras.Model(inputs=model_inputs, outputs=model_output)
    # Call the compile method to transform the layers into a model that
    # Keras can execute.  Notice that we're using a different loss
    # function for classification than for regression.
    model.compile(
        optimizer=keras.optimizers.RMSprop(settings.learning_rate),
        loss=keras.losses.BinaryCrossentropy(),
        metrics=metrics,
    )
    return model


def train_model(
    experiment_name: str,
    model: keras.Model,
    dataset: pd.DataFrame,
    labels: np.ndarray,
    settings: ExperimentSettings,
) -> Experiment:
    """Feed a dataset into the model in order to train it."""

    # The x parameter of keras.Model.fit can be a list of arrays, where
    # each array contains the data for one feature.
    features = {
        feature_name: np.array(dataset[feature_name])
        for feature_name in settings.input_features
    }

    history = model.fit(
        x=features,
        y=labels,
        batch_size=settings.batch_size,
        epochs=settings.number_epochs,
    )

    return Experiment(
        name=experiment_name,
        settings=settings,
        model=model,
        epochs=history.epoch,
        metrics_history=pd.DataFrame(history.history),
    )


print("Defined the create_model and train_model functions.")


# @title Define the plotting function.
def plot_experiment_metrics(experiment: Experiment, metrics: list[str]):
    """Plot a curve of one or more metrics for different epochs."""
    plt.figure(figsize=(12, 8))

    for metric in metrics:
        plt.plot(experiment.epochs, experiment.metrics_history[metric], label=metric)

    plt.xlabel("Epoch")
    plt.ylabel("Metric value")
    plt.grid()
    plt.legend()


print("Defined the plot_curve function.")


# Let's define our first experiment settings.
settings = ExperimentSettings(
    learning_rate=0.001,
    number_epochs=60,
    batch_size=100,
    classification_threshold=0.35,
    input_features=input_features,
)

metrics = [
    keras.metrics.BinaryAccuracy(
        name="accuracy", threshold=settings.classification_threshold
    ),
    keras.metrics.Precision(
        name="precision", thresholds=settings.classification_threshold
    ),
    keras.metrics.Recall(name="recall", thresholds=settings.classification_threshold),
    keras.metrics.AUC(num_thresholds=100, name="auc"),
]

# Establish the model's topography.
model = create_model(settings, metrics)

# Train the model on the training set.
experiment = train_model("baseline", model, train_features, train_labels, settings)

# Plot metrics vs. epochs
plot_experiment_metrics(experiment, ["accuracy", "precision", "recall"])
plot_experiment_metrics(experiment, ["auc"])


def evaluate_experiment(
    experiment: Experiment, test_dataset: pd.DataFrame, test_labels: np.array
) -> dict[str, float]:
    features = {
        feature_name: np.array(test_dataset[feature_name])
        for feature_name in experiment.settings.input_features
    }
    return experiment.model.evaluate(
        x=features,
        y=test_labels,
        batch_size=settings.batch_size,
        verbose=0,  # Hide progress bar
        return_dict=True,
    )


def compare_train_test(experiment: Experiment, test_metrics: dict[str, float]):
    print("Comparing metrics between train and test:")
    for metric, test_value in test_metrics.items():
        print("------")
        print(f"Train {metric}: {experiment.get_final_metric_value(metric):.4f}")
        print(f"Test {metric}:  {test_value:.4f}")


# Evaluate test metrics
test_metrics = evaluate_experiment(experiment, test_features, test_labels)
compare_train_test(experiment, test_metrics)
"""
全特征拟合
"""

all_input_features = [
    "Eccentricity",
    "Major_Axis_Length",
    "Minor_Axis_Length",
    "Area",
    "Convex_Area",
    "Perimeter",
    "Extent",
]

settings_all_features = ExperimentSettings(
    learning_rate=0.001,
    number_epochs=60,
    batch_size=100,
    classification_threshold=0.5,
    input_features=all_input_features,
)

# Modify the following definition of METRICS to generate
# not only accuracy and precision, but also recall:
metrics = [
    keras.metrics.BinaryAccuracy(
        name="accuracy",
        threshold=settings_all_features.classification_threshold,
    ),
    keras.metrics.Precision(
        name="precision",
        thresholds=settings_all_features.classification_threshold,
    ),
    keras.metrics.Recall(
        name="recall", thresholds=settings_all_features.classification_threshold
    ),
    keras.metrics.AUC(num_thresholds=100, name="auc"),
]

# Establish the model's topography.
model_all_features = create_model(settings_all_features, metrics)

# Train the model on the training set.
experiment_all_features = train_model(
    "all features",
    model_all_features,
    train_features,
    train_labels,
    settings_all_features,
)

# Plot metrics vs. epochs
plot_experiment_metrics(experiment_all_features, ["accuracy", "precision", "recall"])
plot_experiment_metrics(experiment_all_features, ["auc"])

test_metrics_all_features = evaluate_experiment(
    experiment_all_features, test_features, test_labels
)
compare_train_test(experiment_all_features, test_metrics_all_features)

# @title Define function to compare experiments


def compare_experiment(
    experiments: list[Experiment],
    metrics_of_interest: list[str],
    test_dataset: pd.DataFrame,
    test_labels: np.array,
):
    # Make sure that we have all the data we need.
    for metric in metrics_of_interest:
        for experiment in experiments:
            if metric not in experiment.metrics_history:
                raise ValueError(
                    f"Metric {metric} not available for experiment {experiment.name}"
                )

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(2, 1, 1)

    colors = [f"C{i}" for i in range(len(experiments))]
    markers = [".", "*", "d", "s", "p", "x"]
    marker_size = 10

    ax.set_title("Train metrics")
    for i, metric in enumerate(metrics_of_interest):
        for j, experiment in enumerate(experiments):
            plt.plot(
                experiment.epochs,
                experiment.metrics_history[metric],
                markevery=4,
                marker=markers[i],
                markersize=marker_size,
                color=colors[j],
            )

    # Add custom legend to show what the colors and markers mean
    legend_handles = []
    for i, metric in enumerate(metrics_of_interest):
        legend_handles.append(
            Line2D(
                [0], [0], label=metric, marker=markers[i], markersize=marker_size, c="k"
            )
        )
    for i, experiment in enumerate(experiments):
        legend_handles.append(Line2D([0], [0], label=experiment.name, color=colors[i]))

    ax.set_xlabel("Epoch")
    ax.set_ylabel("Metric value")
    ax.grid()
    ax.legend(handles=legend_handles)

    ax = fig.add_subplot(2, 1, 2)
    spacing = 0.3
    n_bars = len(experiments)
    bar_width = (1 - spacing) / n_bars
    for i, experiment in enumerate(experiments):
        test_metrics = evaluate_experiment(experiment, test_dataset, test_labels)
        x = np.arange(len(metrics_of_interest)) + bar_width * (i + 1 / 2 - n_bars / 2)
        ax.bar(
            x,
            [test_metrics[metric] for metric in metrics_of_interest],
            width=bar_width,
            label=experiment.name,
        )
    ax.set_xticks(np.arange(len(metrics_of_interest)), metrics_of_interest)

    ax.set_title("Test metrics")
    ax.set_ylabel("Metric value")
    ax.set_axisbelow(True)  # Put the grid behind the bars
    ax.grid()
    ax.legend()


print("Defined function to compare experiments.")
compare_experiment(
    [experiment, experiment_all_features],
    ["accuracy", "auc"],
    test_features,
    test_labels,
)
