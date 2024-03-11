// base64 encoding and decoding

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// base64 encoding
char *base64_encode(const char *data, int data_len) {
  char *p = NULL;
  int i = 0;
  int j = 0;
  char *tmp = NULL;
  char *base64_table =
      "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
  p = (char *)malloc((data_len / 3 + 1) * 4 + 1);
  if (p == NULL) {
    return NULL;
  }
  tmp = p;
  while (i < data_len) {
    char a = 0, b = 0, c = 0;
    if (i < data_len) {
      a = data[i++];
    }
    if (i < data_len) {
      b = data[i++];
    }
    if (i < data_len) {
      c = data[i++];
    }
    p[j++] = base64_table[(a >> 2) & 0x3f];
    p[j++] = base64_table[((a << 4) | (b >> 4)) & 0x3f];
    p[j++] = base64_table[((b << 2) | (c >> 6)) & 0x3f];
    p[j++] = base64_table[c & 0x3f];
  }
  switch (data_len % 3) {
  case 1:
    p[j - 1] = '=';
  case 2:
    p[j - 2] = '=';
  }
  p[j] = '\0';
  return tmp;
}

// base64 decoding
char *base64_decode(const char *data, int data_len) {
  char *p = NULL;
  int i = 0;
  int j = 0;
  char *tmp = NULL;
  char *base64_table =
      "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
  p = (char *)malloc(data_len * 3 / 4 + 1);
  if (p == NULL) {
    return NULL;
  }
  tmp = p;
  while (i < data_len) {
    char a = 0, b = 0, c = 0, d = 0;
    if (i < data_len) {
      a = strchr(base64_table, data[i++]) - base64_table;
      b = strchr(base64_table, data[i++]) - base64_table;
      c = strchr(base64_table, data[i++]) - base64_table;
      d = strchr(base64_table, data[i++]) - base64_table;
    }
    p[j++] = (a << 2) | (b >> 4);
    p[j++] = (b << 4) | (c >> 2);
    p[j++] = (c << 6) | d;
  }
  if (data[data_len - 1] == '=') {
    j--;
    if (data[data_len - 2] == '=') {
      j--;
    }
  }
  p[j] = '\0';
  return tmp;
}

int main() {
  char *data = "hello world";
  char *p = base64_encode(data, strlen(data));
  printf("%s\n", p);
  free(p);

  char *p2 = base64_decode(p, strlen(p));
  printf("%s\n", p2);
  free(p2);
  return 0;
}
