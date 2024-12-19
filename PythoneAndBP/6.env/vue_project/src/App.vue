<template>
  <div id="app" class="hide-scrollbar">
    <!-- <img alt="Vue logo" src="./assets/logo.png" /> -->
    <!-- <h1>{{ message }}</h1> -->
    <!-- <p>Request URL: {{ requestUrl }}</p> -->
    <!-- <p>{{ data }}</p> -->
    <el-form :inline="true" :model="formInline" class="demo-form-inline">
      <el-form-item label="">
        <el-input v-model="formInline.capital" placeholder="capital"></el-input>
      </el-form-item>
      <el-form-item label="">
        <el-input v-model="formInline.country" placeholder="country"></el-input>
      </el-form-item>
      <el-form-item label="">
        <el-input
          v-model="formInline.longitude"
          placeholder="longitude"
        ></el-input>
      </el-form-item>
      <el-form-item label="">
        <el-input
          v-model="formInline.latitude"
          placeholder="latitude"
        ></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="add">New</el-button>
      </el-form-item>
    </el-form>
    <el-divider></el-divider>
    <el-table
      :data="data"
      style="width: 100%"
      max-height="400"
      v-loading="loading"
    >
      <el-table-column label="city">
        <template slot-scope="scope">
          <i class="el-icon-time"></i>
          <span style="margin-left: 10px">{{ scope.row.city }}</span>
        </template>
      </el-table-column>
      <el-table-column label="country">
        <template slot-scope="scope">
          <i class="el-icon-time"></i>
          <span style="margin-left: 10px">{{ scope.row.country }}</span>
        </template>
      </el-table-column>
      <el-table-column label="temperature">
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
            <p>
              Country：<el-tag type="success">{{ scope.row.country }}</el-tag>
            </p>
            <p>
              City：
              <el-tag type="danger" effect="plain">{{ scope.row.city }}</el-tag>
            </p>
            <div slot="reference" class="name-wrapper">
              <el-tag size="medium">{{ scope.row.temperature }}</el-tag>
            </div>
          </el-popover>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <!-- <el-button size="mini" @click="handleEdit(scope.$index, scope.row)"
            >编辑</el-button
          > -->
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)"
            >Delete</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
const comurl = "http://127.0.0.1:8000";
async function fetchData(method, url, body = null) {
  const options = {
    method: method, // 请求方法
    headers: {
      "Content-Type": "application/json", // 设置请求头
    },
  };

  // 如果是 POST DELETE 请求，添加请求体
  if (method !== "GET" && body) {
    options.body = JSON.stringify(body);
  }

  try {
    const response = await fetch(url, options);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json(); // 返回 JSON 数据
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error; // 抛出错误以便在调用时处理
  }
}
export default {
  data() {
    return {
      message: "",
      requestUrl: "",
      data: null,
      loading: true,
      formInline: {
        capital: "",
        country: "",
        longitude: "",
        latitude: "",
      },
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      this.loading = true;
      try {
        const result = await fetchData("GET", comurl + "/F5");
        this.message = result.message; // 从响应中获取message
        this.requestUrl = result.request; // 从响应中获取requestUrl
        this.notifysuc(this.message, this.requestUrl);
        console.log(result);

        this.data = result.data; // 从响应中获取data
      } catch (error) {
        // 处理错误
        this.notifyfail("错误", "数据加载失败");
      } finally {
        this.loading = false; // 无论成功与否都要关闭 loading
      }
    },

    async postData(url, body) {
      this.loading = true;
      try {
        // const body = this.formInline;
        const result = await fetchData("POST", comurl + url, body);
        console.log(result);

        this.data = [result.data, ...this.data];
        // 处理返回的数据
        this.notifysuc("成功", "数据已成功提交");
      } catch (error) {
        // 处理错误
        this.notifyfail("错误", "数据提交失败");
      } finally {
        this.loading = false; // 无论成功与否都要关闭 loading
      }
    },
    async handleDelete(index, row) {
      this.loading = true;
      try {
        const result = await fetchData("DELETE", comurl + "/delete", {
          city: row.city,
          country: row.country,
        });
        // 从 data 中移除已删除的项
        this.data = this.data.filter(
          (item) => item.city !== row.city || item.country !== row.country
        );
        console.log(result);
        this.notifysuc("成功", "数据已成功删除");
      } catch (error) {
        this.notifyfail("错误", "数据删除失败");
      } finally {
        this.loading = false;
      }
    },
    add() {
      const hasEmpty = Object.values(this.formInline).some(
        (value) => value == ""
      );
      if (hasEmpty) {
        this.notifyfail("错误", "请填写所有字段");
        return;
      }
      let { longitude, latitude } = this.formInline;
      // 验证经度
      if (isNaN(longitude) || longitude < -180 || longitude > 180) {
        this.notifyfail("错误", "经度必须在 -180 到 180 之间");
        return;
      }

      // 验证纬度
      if (isNaN(latitude) || latitude < -90 || latitude > 90) {
        this.notifyfail("错误", "纬度必须在 -90 到 90 之间");
        return;
      }
      // 继续处理表单提交
      this.postData("/add", this.formInline);
    },

    notifysuc(title, message) {
      this.$notify({
        title,
        message,
        type: "success",
        // duration: 0,
        position: "bottom-right",
      });
    },
    notifyfail(title, message) {
      this.$notify({
        title,
        message,
        type: "error",
        position: "bottom-right",
      });
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#app {
  display: flex;
  flex-direction: column;
  /* align-items: center; 水平居中 */
  justify-content: center; /* 垂直居中 */
  /* height: 100vh; 使容器占满整个视口高度  */
}

.el-table {
  flex: 1; /* 使表格在容器中弹性伸缩 */
  min-width: 600px; /* 设置最小宽度 */
}
</style>
