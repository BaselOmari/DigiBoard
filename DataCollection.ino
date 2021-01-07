
#include "Adafruit_MCP23017.h"

void fill_board(bool board[]);
bool board_change(bool const new_board[], bool const old_board[]);
void add_str_board(bool board[]);

Adafruit_MCP23017 mcp1;
Adafruit_MCP23017 mcp2;
Adafruit_MCP23017 mcp3;
Adafruit_MCP23017 mcp4;

bool old_board[64]{};
bool new_board[64]{};
String str_board{};
int const clock_Pin = 2;
int const reset_Pin = 3;
int clock_state{};
int reset_state{};


void setup() {
  Serial.begin(19200);

  pinMode(clock_Pin, INPUT);
  pinMode(reset_Pin, INPUT);
  
  mcp1.begin();
  mcp2.begin(1);
  mcp3.begin(2);
  mcp4.begin(3);

  for(int i = 0; i <= 15; i++) {
    mcp1.pinMode(i, INPUT);
    mcp2.pinMode(i, INPUT);
    mcp3.pinMode(i, INPUT);
    mcp4.pinMode(i, INPUT);
  }
}

void loop() {

  clock_state = digitalRead(clock_Pin);
  reset_state = digitalRead(reset_Pin);
  
  fill_board(new_board);
  if (board_change(new_board,old_board))
  {
    add_str_board(new_board);
  }

  if (clock_state == HIGH)
  {
    Serial.println(str_board);
    resets();
  }

  if (reset_state == HIGH)
  {
    resets();
  }
  
  
  for (int i = 0; i < 64; i++)
  {
    old_board[i] = new_board[i];
  }
}

bool board_change(bool const new_board[], bool const old_board[])
{
  for (int i = 0; i < 64; i++)
  {
    if (new_board[i] != old_board[i])
    {
      return true;
    }
  }

  return false;
}

void fill_board(bool board[])
{
  Adafruit_MCP23017 mcps[4] = {mcp1,mcp2,mcp3,mcp4};

  for (int mcp = 0; mcp < 4; mcp++)
  {
    for (int i = 0; i < 16; i++)
    {
      board[i+mcp*16] = mcps[mcp].digitalRead(i);
    }
  }
}

void add_str_board(bool board[])
{
  for (int i = 0; i < 64; i++)
  {
    str_board += String(board[i]);
  }
}

void resets()
{
  for (int i = 0; i < 64; i++)
  {
    old_board[i] = 0;
    new_board[i] = 0;
  }

  str_board = "";
}
