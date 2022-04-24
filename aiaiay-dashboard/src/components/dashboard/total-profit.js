import { Avatar, Card, CardContent, Grid, Typography } from '@mui/material';
import AttachMoneyIcon from '@mui/icons-material/AttachMoney';
import { Button } from '@mui/material';

export const TotalProfit = (props) => (
                           <Card {...props}>
                             <CardContent>
                               <Grid
                                 container
                                 spacing={3}
                                 sx={{ justifyContent: 'space-between' }}
                               >
                                 <Grid item>
                                   <Typography
                                     color="textSecondary"
                                     gutterBottom
                                     variant="overline"
                                   >
                                     EXTREME WEATHER HAZARDS IN THE WORLD
                                   </Typography>
                                   <Typography
                                     color="red"
                                     variant="h4"
                                   >
                                     21 % at high risk
                                   </Typography>
                                    <Button variant="contained" onClick={(e) => {
                                                                                        e.preventDefault();
                                                                                        window.location.href='/hazards.html';
                                                                                        }}
                                                                                  >View our dashboard</Button>
                                 </Grid>
                                 <Grid item>
                                   <Avatar
                                     sx={{
                                       backgroundColor: 'success.main',
                                       height: 56,
                                       width: 56
                                     }}
                                   >
                                   </Avatar>
                                 </Grid>
                               </Grid>
                             </CardContent>
                           </Card>
                         );
